import torch
import torch.nn as nn
import torch.nn.init as init
import torch.nn.functional as F
import math
import sys
import numpy as np
import pdb
import os

import time
from itertools import chain

from datetime import datetime
from perforatedai import globals_perforatedai as GPA
from perforatedai import modules_perforatedai as MPA
from perforatedbp import check_license
import copy
import random


# This is the list of values that get added to each dendrite module for each dendrite
def update_dendrite_tensor_values(DENDRITE_TENSOR_VALUES):
    return DENDRITE_TENSOR_VALUES + [
        "top_dendrite_candidate_averages",
        "prev_dendrite_candidate_correlation",
        "current_correlations_for_parallel",
        "best_score",
        "previous_best_score",
        "prev_dendrite_candidate_average",
        "main_grad_average_for_scaling",
        "candidate_grad_average_for_scaling",
        "indexes_of_best",
        "nodes_best_improved_this_epoch",
        "parents_average_d_vector",
        "normal_pass_average_d",
    ]


# Same as above but these are single value tensors
def update_dendrite_single_values(DENDRITE_SINGLE_VALUES):
    return DENDRITE_SINGLE_VALUES + [
        "breaking",
        "locked",
        "best_score_improved_this_time_step",
        "best_score_improved_this_epoch",
    ]


# These are included above, they just get skipped for reinit if not live
NON_LIVE_SKIP_VALUES = [
    "normal_pass_average_d",
]


if GPA.pc.get_doing_thing():
    DENDRITE_SINGLE_VALUES = DENDRITE_SINGLE_VALUES + [
        "normal_pass_max_mean_act",
        "parent_max_mean_act",
    ]
    NON_LIVE_SKIP_VALUES = NON_LIVE_SKIP_VALUES + ["normal_pass_max_mean_act"]


def update_value_tracker_arrays(VALUE_TRACKER_ARRAYS):
    return VALUE_TRACKER_ARRAYS + ["current_parent_d"]


def get_tuples_and_mult(val, values):
    """
    This function uses this_node_index to create returned values
        math_tuple - tuple of dimensions to do math over
        view_tuple - tuple of dimensions to view with -1 at this_node_index
        full_mult - product of all dimensions except this_node_index
    """
    math_tuple = []
    view_tuple = []
    full_mult = 1
    for i in range(len(val.size())):
        if i == values.this_node_index:
            view_tuple.append(-1)
            continue
        full_mult *= val.shape[i]
        math_tuple.append(i)
        view_tuple.append(1)
    return math_tuple, view_tuple, full_mult


def filter_backward_pb(val, values, candidate_nonlinear_outs):
    # TODO: move torch.no_grad to modules_perforatedai
    with torch.no_grad():
        math_tuple, view_tuple, full_mult = get_tuples_and_mult(val, values[0])
        if GPA.pai_tracker.member_vars["mode"] == "p":
            for i in range(0, GPA.pc.get_global_candidates()):
                # this is where the grad_in is actually set for the tagger
                average_d_matrix = values[i].parents_average_d_vector.view(view_tuple)
                if val.device.type == "cpu":
                    device_index = 0
                else:
                    device_index = val.device.index
                if (
                    GPA.pc.get_debugging_memory_leak()
                    and len(values[i].current_parent_d[device_index]) != 0
                ):
                    print(
                        "%s called backward but then didn't get PAIified.  This can cause a memory leak. Check processors."
                        % values[i].layer_name
                    )
                if len(candidate_nonlinear_outs) == 0:
                    print(
                        "Trying to call backwards but module %s wasn't PAIified"
                        % values[i].layer_name
                    )
                    sys.exit(0)
                # For now dendrite_learn_mode just means doing Cascor.
                if GPA.pc.get_dendrite_learn_mode():
                    # This line will set current_parent_d to be the current error - the average error
                    values[i].current_parent_d[device_index].append(
                        (val - (average_d_matrix)).detach()
                    )
                    # Then the output of the dendrites, after the nonlinearity, is told to use that value as its error signal
                    candidate_nonlinear_outs[i].register_hook(
                        lambda grad: values[i]
                        .current_parent_d[device_index][-1]
                        .to(val.device)
                    )
                # pretty sure this next line is the right way to do this, not above.  doesn't seem to really have any significant impact though.  should run normal unit tests and xor_main with it to be sure.
                # Values[i].current_parent_d = (val).detach()
                # candidate_nonlinear_outs[i].register_hook(lambda grad: (Values[i].current_parent_d  - (Values[i].parents_average_d_matrix)))
        try:
            # update the running average with the current error
            values[0].normal_pass_average_d *= 0.99
            values[0].normal_pass_average_d += (val.sum(math_tuple) * 0.01) / full_mult
            if GPA.pc.get_dpp_verbose():
                print("no error with")
                print(val.shape)
                print(values[0].this_node_index)
                print(math_tuple)
                print(full_mult)
        except Exception as e:
            print(e)
            print("Error with type shape in %s" % values[0].layer_name)
            print(val.shape)
            print(values[0].this_node_index)
            print(math_tuple)
            print(full_mult)
            import pdb

            pdb.set_trace()
            exit(0)

        # Should get rid of the below comments (and others here) after CC is verified

        # values[0].normal_pass_average_d_mags *= 0.99
        # values[0].normal_pass_average_d_mags += (val.abs().sum(math_tuple) * 0.01) / full_mult
        # values[0].normal_pass_average_d_std = values[0].normal_pass_average_d_std * 0.99 + val.std((math_tuple))*0.01

        # this is **2 after everything because it is a scalar to scale the final grad_in.  The final gradient that actually gets applied is gradient.sum(math_tuple)
        # final weight adjustment/actual grad value is net.module.main_module[0].PAINeuronModule.current_d.sum(math_tuple)
        # You can tell this by looking at the bias values in grad.  It will be similar for the convolution kernel weight values in grad
        """
        values[0].normal_pass_average_d_sq *= 0.99
        if(GPA.pc.get_grad_sum_first()):
            values[0].normal_pass_average_d_sq += ((val)**2).sum(math_tuple) * 0.01# / full_mult #if changing here change previous in data parallel
        else:
            values[0].normal_pass_average_d_sq += ((val)).sum(math_tuple)**2 * 0.01# / full_mult
        """

        # if trying to do cascor with dendrites while also updating neurons
        # the parents average d needs to be a running average as well isntead of a final average
        # TODO: if not doing this, perhaps we could save compute costs by not doing all this summing and averaging
        # during the 100 training iterations, and isntead just do it once in between N and P switches
        if GPA.pc.get_learn_dendrites_live():

            # Keep these values updated on the fly  if this works, might only need to do mean, above and will stay the same and be faster.
            values[0].parents_average_d_vector.copy_(
                values[0].normal_pass_average_d.detach().clone() / (full_mult)
            )
            values[0].parents_average_d_vector.requires_grad = False

    if GPA.pc.get_extra_verbose():
        print("%s completing backward" % values[0].layer_name)


def set_grad_params(model, to_set):
    """Set requires_grad for all parameters in a model"""
    for p in model.parameters():
        p.requires_grad = to_set


def set_module_n_pb(neuron_module):
    """Set the module to n mode - this means the main module learns and the dendrites do not"""
    set_grad_params(neuron_module.main_module, True)
    # pb to top [x] is a nodes_x_dendrite_module array, dont need to loop since older ones arent used
    if neuron_module.dendrite_modules_added > 0:
        neuron_module.dendrites_to_top[
            neuron_module.dendrite_modules_added - 1
        ].requires_grad = True
    for param in neuron_module.dendrite_module.dendrites_to_dendrites:
        # TODO: after checking that exact values passes this should be GPA.pc.get_dendrite_update_mode()
        param.requires_grad = False


def set_module_p_pb(neuron_module):
    """Set the module to p mode - this means the dendrites learn and the main module does not"""
    if GPA.pc.get_learn_dendrites_live():
        # If learning live the candidates need to also connect to top so add them here
        neuron_module.candidate_to_top = nn.Parameter(
            torch.zeros(
                (1, neuron_module.out_channels),
                device=GPA.pc.get_device(),
                dtype=GPA.pc.get_d_type(),
            )
            .detach()
            .clone(),
            requires_grad=True,
        )
        neuron_module.register_parameter(
            "current_candidate_to_top", neuron_module.candidate_to_top
        )
        set_grad_params(neuron_module.main_module, True)
        # pb to top [x] is a nodes_x_dendrite_module array, no loop required since
        if neuron_module.dendrite_modules_added > 0:
            neuron_module.dendrites_to_top[
                neuron_module.dendrite_modules_added - 1
            ].requires_grad = True
            for param in neuron_module.dendrite_module.dendrites_to_dendrites:
                param.requires_grad = True

    # Set all parameters in established network to no longer learn
    else:
        set_grad_params(neuron_module.main_module, False)
        if neuron_module.dendrite_modules_added > 0:
            neuron_module.dendrites_to_top[
                neuron_module.dendrite_modules_added - 1
            ].requires_grad = False
            for param in neuron_module.dendrite_module.dendrites_to_dendrites:
                param.requires_grad = False


def load_tagger_values(neuron_module):
    neuron_module.dendrite_module.load_tagger_values()


def apply_pb(
    neuron_module,
    out,
    candidate_outs,
    candidate_nonlinear_outs,
    candidate_outs_non_zeroed,
):
    """
    During P mode this plugs the candidates outputs
    into the autograd graph through the out tensor
    NOTE: this is plugged in before the nonlinearity - is this correct?
    """
    if (
        GPA.pai_tracker.member_vars["mode"] == "p"
        and neuron_module.dendrite_module.mode == "p"
    ):
        ## NEED LOOP HERE
        for i in range(0, GPA.pc.get_global_candidates()):
            # If learning live, actually add the non-zeroed outputs
            if GPA.pc.get_learn_dendrites_live():
                # TODO: can this be replace with the get tuples function?
                to_top = neuron_module.candidate_to_top[i, :]
                for dim in range(len(candidate_outs_non_zeroed[i].shape)):
                    if dim == neuron_module.this_node_index:
                        continue
                    to_top = to_top.unsqueeze(dim)
                if GPA.pc.get_confirm_correct_sizes():
                    to_top = to_top.expand(
                        list(candidate_outs_non_zeroed[i].size())[
                            0 : neuron_module.this_node_index
                        ]
                        + [neuron_module.out_channels]
                        + list(candidate_outs_non_zeroed[i].size())[
                            neuron_module.this_node_index :
                        ]
                    )
                out = out + (
                    candidate_outs_non_zeroed[i].to(out.device) * to_top.to(out.device)
                )

            # add the zeroed outputs
            out = out + candidate_outs[i].to(out.device)

    # doing_thing means keeping track of the max activation, this is where that is calculated
    if GPA.pai_tracker.member_vars["mode"] == "n" and GPA.pc.get_doing_thing():
        if (
            out.abs().max()
            > neuron_module.dendrite_module.dendrite_values[0].normal_pass_max_mean_act
        ):
            neuron_module.dendrite_module.dendrite_values[0].normal_pass_max_mean_act[
                0
            ] = (out.abs().max().item())
            if GPA.pc.get_learn_dendrites_live():
                neuron_module.dendrite_module.dendrite_values[
                    0
                ].parent_max_mean_act.copy_(
                    neuron_module.dendrite_module.dendrite_values[0]
                    .normal_pass_max_mean_act[0]
                    .detach()
                    .clone()
                )
                neuron_module.dendrite_module.dendrite_values[
                    0
                ].parent_max_mean_act.requires_grad = False
        if (
            neuron_module.dendrite_module.dendrite_values[0].normal_pass_max_mean_act[0]
            == 0
        ):
            print("An entire layer got exactly 0 Correlation")
    return out


def setup_hooks(neuron_module, out, candidate_nonlinear_outs):
    """
    if there are not nonlinear outs, then this module was not PAIified,
    so just call the regular filter_backward
    otherwise call filter_backward with the candidate nonlinear outs
    """
    if candidate_nonlinear_outs == {}:
        out.register_hook(
            lambda grad: MPA.filter_backward(
                grad, neuron_module.dendrite_module.dendrite_values, {}
            )
        )
    else:
        candidate_nonlinear_outs[0] = candidate_nonlinear_outs[0].to(out.device)
        out.register_hook(
            lambda grad: MPA.filter_backward(
                grad,
                neuron_module.dendrite_module.dendrite_values,
                candidate_nonlinear_outs,
            )
        )


def create_extra_tensors(dendrite_module):
    """
    for DendriteModules this creates the extra tensors needed for Cascor
    """
    # Saved tensors for recurrent modules
    dendrite_module.current_recurrent_pass_tensors = []
    dendrite_module.current_recurrent_pass_candidate_tensors = []
    # PAI VALUES
    dendrite_module.normal_learning_taggers = {}

    dendrite_module.random_pai_to_candidates = (
        GPA.pc.get_default_random_pai_to_candidates()
    )


def init_candidates(dendrite_module, j):
    """
    Randomizes the candidates to dendrites weights
    TODO: Should this also include the same dendrite multiplier?
    """
    dendrite_module.dendrites_to_candidates[j].data.pai_wrapped = True
    if dendrite_module.random_pai_to_candidates:
        with torch.no_grad():
            dendrite_module.dendrites_to_candidates[j].normal_(
                0, math.sqrt(2.0 / dendrite_module.out_channels)
            )
    # dendrite_module.register_parameter(('dendrites_to_candidates'+str(j)), dendrite_module.dendrites_to_candidates[j])


def set_pb_mode(dendrite_module, mode):
    if mode == "n":
        if GPA.pc.get_verbose():
            print("so calling all the things to add to layers")
        for i in range(0, GPA.pc.get_global_candidates()):
            dendrite_module.dendrite_values[i].locked[0] = 1

        # Set each main modules parameters to learn based on dendrite_update_mode
        set_grad_params(
            dendrite_module.layers[dendrite_module.num_dendrites],
            GPA.pc.get_dendrite_update_mode(),
        )
        # Set the additional input parameters from other dendrites the same
        for param in dendrite_module.dendrites_to_dendrites:
            param.requires_grad = GPA.pc.get_dendrite_update_mode()

        # TODO: this might not be needed as the candidates are no longer used in n_mode
        # if this is included because of learn_live, then requires grad should be True?
        if dendrite_module.num_dendrites > 0:
            for j in range(0, GPA.pc.get_global_candidates()):
                dendrite_module.dendrites_to_candidates[j].requires_grad = False


def killer_recursive(in_vals, killing):
    """
    If killing is true go through in_vals and kill all of the tensor gradients
    If killing is false, this function is still required to return the correct device
    """
    # Check license every 0.000001% of the time, this should also have been checked in convert network
    # Checking additionally here since check can be easily removed from convert network in open source
    if random.random() < 0.000001:
        license_file = "./license.yaml"
        status = check_license.valid_license(license_file)
        if not status:
            print("License Invalid. Quiting...")
            sys.exit(1)
    # Go through the in_vals of various types and either continue recursing
    # or kill the gradients if it is a tensor
    device = None
    if type(in_vals) is list:
        if len(in_vals) == 0:
            return in_vals, None
        for index in range(len(in_vals)):
            in_vals[index], device2 = killer_recursive(in_vals[index], killing)
            if not device2 is None:
                device = device2
    elif type(in_vals) is tuple:
        if len(in_vals) == 0:
            return in_vals, None
        for index in range(len(in_vals)):
            in_vals = list(in_vals)
            in_vals[index], device2 = killer_recursive(in_vals[index], killing)
            if not device2 is None:
                device = device2
            in_vals = tuple(in_vals)
    elif type(in_vals) is dict:
        if len(in_vals.keys()) == 0:
            return in_vals, None
        for index in in_vals.keys():
            in_vals[index], device2 = killer_recursive(in_vals[index], killing)
            if not device2 is None:
                device = device2
    elif issubclass(torch.Tensor, type(in_vals)):
        with torch.cuda.device_of(in_vals):
            if killing:
                to_return = grad_killer(in_vals).detach().clone()
            else:
                to_return = in_vals
            return to_return, in_vals.device
    else:
        return in_vals, None
    return in_vals, device


def preprocess_pb(*args, **kwargs):
    """
    Applies killer to args and kwargs
    """
    args2, device = killer_recursive(args, GPA.pc.get_dendrite_graph_mode())
    kwargs2, device2 = killer_recursive(kwargs, GPA.pc.get_dendrite_graph_mode())
    return args2, kwargs2


def add_dendrite_inputs(dendrite_module, i, candidate_outs, outs, view_tuple, device):
    for in_index in range(dendrite_module.num_dendrites):
        # This is only the case when passing a single datapoint rather than a batch
        if view_tuple == [1]:
            candidate_outs = (
                candidate_outs.to(device)
                + dendrite_module.dendrites_to_candidates[i][in_index, :].to(device)
                * outs[in_index]
            )
        else:
            candidate_outs = (
                candidate_outs.to(device)
                + dendrite_module.dendrites_to_candidates[i][in_index, :]
                .view(view_tuple)
                .to(device)
                * outs[in_index]
            )
    return candidate_outs


def forward_candidates(dendrite_module, view_tuple, outs, *args, **kwargs):
    """
    This is the main forward function to process dendrite candidates
    """
    # candidate_outs is a dict for the outs which have already been zeroed and nonlinearity applied
    candidate_outs = {}
    # candidate_nonlinear_outs is a dict for the output values after the nonlinearity
    candidate_nonlinear_outs = {}
    # candidate_non_zeroed is a dict for the outputs which have not been zeroed but not yet had nonlinearity applied
    candidate_non_zeroed = {}

    for i in range(0, GPA.pc.get_global_candidates()):
        # dendrite_module.mode will only not also be p if this is not learning
        if GPA.pai_tracker.member_vars["mode"] == "p" and dendrite_module.mode == "p":
            # first apply killer to the inputs and get the device
            args2, device = killer_recursive(args, GPA.pc.get_candidate_graph_mode())
            kwargs2, device2 = killer_recursive(
                kwargs, GPA.pc.get_candidate_graph_mode()
            )
            if device is None:
                device = device2

            """
            DEBUG: if you\'re here this layer should have PAI nodes which means
            candidate processors should have been initialized.  If its not you are likely
            still pointing to the old model that doesn\'t have PAI nodes added.  make sure
            when you call add validation score you are properly setting the model
            """
            # Call processors on the killed inputs
            if dendrite_module.candidate_processors != []:
                args2, kwargs2 = dendrite_module.candidate_processors[i].pre_d(
                    *args2, **kwargs2
                )

            """
            DEBUG:
            If you are getting a cpu vs gpu issue on this line its because the model is receiving args that are on the wrong device,
            but within the forward function it gets passed to the correct spot.  
            don't ever call to() in the forward function, call it before it gets passed in.
            """
            # Pass the inputs through the candidate module
            candidate_out_values = dendrite_module.candidate_module[i].to(device)(
                *args2, **kwargs2
            )
            # Post process the candidates output
            if dendrite_module.candidate_processors != []:
                candidate_outs[i] = dendrite_module.candidate_processors[i].post_d(
                    candidate_out_values
                )
            else:
                candidate_outs[i] = candidate_out_values

            # Add to the candidate output the dendrite outputs * dendrite_to_candidates weights
            candidate_outs[i] = add_dendrite_inputs(
                dendrite_module, i, candidate_outs[i], outs, view_tuple, device
            )

            # Tag the candidate out so it will be passed to the Cascor backward function
            # With the associated dendrite_values
            if GPA.pc.get_dendrite_learn_mode():
                candidate_outs[i] = pai_tagger(
                    candidate_outs[i], dendrite_module.dendrite_values[i].to(device)
                )

            # Apply nonlinearty
            candidate_nonlinear_outs[i] = GPA.pc.get_pai_forward_function()(
                candidate_outs[i]
            ).to(device)

            # candidate_nonlinear_outs chosen randomly, just generally saying dont do this during inference, only training.
            if dendrite_module.training:
                # no it seems like this should be cleared on the main module so when its replicated it should work properly.
                if device.type == "cpu":
                    device_index = 0
                else:
                    device_index = device.index
                if (
                    GPA.pc.get_debugging_memory_leak()
                    and len(
                        dendrite_module.dendrite_values[i].dendrite_outs[device_index]
                    )
                    != 0
                ):
                    # this is a flag that can be set to debug memory leaks
                    # it should not be required but for incorrect implementations this sometimes fixes issues without downside.
                    # Just deletes additional tensors that have been incorrectly accumulated to the list
                    if GPA.pc.get_no_backward_workaround():
                        del dendrite_module.dendrite_values[i].dendrite_outs[
                            device_index
                        ][-1]
                        # Following may also be required for no_backward_workaround.  Found it earlier, but didn't have a noBackwards problem to debug with
                        # del dendrite_module.dendrite_values[i].current_parent_d[device_index][-1]
                    else:
                        print(
                            "%s is in backwards graph multiple times."
                            % dendrite_module.name
                        )
                        a = len(dendrite_module.dendrite_values[0].dendrite_outs[0])
                        b = len(dendrite_module.dendrite_values[0].current_parent_d[0])
                        print(
                            "This will cause a memory leak unless it is a recurrent layer."
                        )
                        print("Currently stacked (%d/%d) times" % (a, b))

                        print(
                            "If this is coming up before a memory leak that happens anywhere "
                            + "other than the first batch of an epoch you NEED to debug this."
                        )
                        print("Check the Memory Leak section of the debugging MD file.")
                        print(
                            "If this is just being printed but there is not a memory leak"
                            + " you can set GPA.pc.set_debugging_memory_leak(False)"
                        )
                        print(
                            "If you don't have any recurrent layers you can also clear this by"
                            + " in a more memory efficient way by setting GPA.pc.set_no_backward_workaround(True)"
                        )
                        print(
                            "If you set GPA.pc.set_no_backward_workaround(True) and it causes a"
                            + " IndexError: list index out of range error, that means you do have a recurrent layer"
                        )
                # if doing CC learning add the nonlinear outs to the dendrite values for access during backward
                if GPA.pc.get_dendrite_learn_mode():
                    dendrite_module.dendrite_values[i].dendrite_outs[
                        device_index
                    ].append(candidate_nonlinear_outs[i].detach().clone().to(device))
                    if (
                        GPA.pc.get_extra_verbose()
                        and candidate_nonlinear_outs[i].isnan().any()
                    ):
                        print("got candidate out nan")
                        import pdb

                        pdb.set_trace()
            # Save the non zeroed version and zero the main version
            candidate_non_zeroed[i] = (
                candidate_nonlinear_outs[i].detach().clone().to(device)
            )
            candidate_outs[i] = no_forward(candidate_nonlinear_outs[i])

    return candidate_outs, candidate_nonlinear_outs, candidate_non_zeroed


def check_dendrite_outs(values, device_index):
    """
    This function checks that the outputs and current parent d lists are the correct length
    """
    if len(values.dendrite_outs[device_index]) == 0:
        print("Dendrite does not have output Value for layer %s" % values.layer_name)
        print(
            "This is caused by your model being in eval mode when you call loss.backwards()"
        )
        import pdb

        pdb.set_trace()


def new_best(saved_values):
    """
    This function checks if the new correlation is better than the previous best
    and returns the updated best score and indexes of best scores
    """
    temp_abs = saved_values.prev_dendrite_candidate_correlation.detach().abs()
    # best score is the max score of the previous best score and the current recently averaged correlation
    [best_score, best_indices] = torch.max(
        torch.cat(
            (
                saved_values.best_score.unsqueeze(0),
                temp_abs.unsqueeze(0),
            ),
            0,
        ),
        0,
    )
    return best_score, best_indices


def dendrite_score_beats_current_best(new_score, old_score):
    """
    Returns if any neurons new score is better than the old score by the required percentage and raw amount
    """
    return (
        ((new_score * (1.0 - GPA.pc.get_pai_improvement_threshold()))) > old_score
    ).any() and (
        (new_score - GPA.pc.get_pai_improvement_threshold_raw()) > old_score
    ).any()


def update_saved_values_averages_initial(
    saved_values, current_correlations, grad_in, last_parent_d, math_tuple
):
    # for the first x iterations average out the initial conditions a little bit
    # at the beginning have it equal the actual average, not the abs average
    # this is because the best is the abs of running best
    # but running best is average of a bunch of positives and negatives
    # so to just initialize as a single value it it a high positive or negative

    saved_values.candidate_grad_average_for_scaling *= saved_values.initialized
    saved_values.candidate_grad_average_for_scaling += grad_in.abs().mean(math_tuple)
    saved_values.candidate_grad_average_for_scaling /= saved_values.initialized + 1.0
    saved_values.main_grad_average_for_scaling *= saved_values.initialized
    saved_values.main_grad_average_for_scaling += last_parent_d.abs().mean(math_tuple)
    saved_values.main_grad_average_for_scaling /= saved_values.initialized + 1.0

    saved_values.prev_dendrite_candidate_average *= saved_values.initialized
    saved_values.prev_dendrite_candidate_average += (
        saved_values.top_dendrite_candidate_averages
    )
    saved_values.prev_dendrite_candidate_average /= saved_values.initialized + 1.0
    # This looks like the same equation as above?  Not sure why I have this twice 9.25.2025
    cor = current_correlations - (
        saved_values.prev_dendrite_candidate_average
        * saved_values.parents_average_d_vector
    )  # / net['layers'][l]['sumSqError'][j]

    saved_values.prev_dendrite_candidate_correlation *= saved_values.initialized
    saved_values.prev_dendrite_candidate_correlation += cor
    saved_values.prev_dendrite_candidate_correlation /= saved_values.initialized + 1.0
    # If not initialized yet, maintain best scores as 0
    saved_values.best_score.copy_(saved_values.best_score.detach() * 0)
    saved_values.previous_best_score.copy_(
        saved_values.previous_best_score.detach() * 0
    )
    saved_values.initialized += 1.0


from packaging import version

if version.parse(torch.__version__) >= version.parse("2.4.0"):
    from torch.amp import custom_fwd, custom_bwd
else:
    from torch.cuda.amp import custom_fwd, custom_bwd


def pai_tagger(inp, Values):
    """
    This is the class that takes in the cascor variables and returns a grad_in
    which is the correct gradient for the dendrite candidates
    """

    class Tagger(torch.autograd.Function):
        # Potentially add staticmethod back later, but this doesnt work in compiled version
        # TODO: cast_inputs as GPA.get_precision?
        # @staticmethod
        @custom_fwd(device_type="cuda", cast_inputs=torch.float32)
        def forward(ctx, inp):
            return inp

        # Potentially add staticmethod back later, but this doesnt work in compiled version
        # @staticmethod
        @custom_bwd(device_type="cuda")
        def backward(ctx, grad_out):
            # If things have worked correctly, grad_out here should be (val - average_d_matrix)
            # which then has subsequently gone through the autograd process through the nonlinear functions backwards.

            # Check license every 0.000001% of the time, this should also have been checked in convert network
            if random.random() < 0.000001:
                license_file = "./license.yaml"
                status = check_license.valid_license(license_file)
                if not status:
                    print("License Invalid. Quiting...")
                    sys.exit(1)

            with torch.no_grad():
                saved_values = Values
                if GPA.pc.get_extra_verbose():
                    print("%s calling Dendrite backward" % saved_values.layer_name)
                # If locked just return 0 gradient
                if saved_values.locked:
                    return grad_out * 0, None

                # Compute initial settings for the rest of the function
                math_tuple, view_tuple, full_mult = get_tuples_and_mult(
                    grad_out, saved_values
                )
                eps = 0.00000001
                if grad_out.device.type == "cpu":
                    device_index = 0
                else:
                    device_index = grad_out.device.index
                check_dendrite_outs(saved_values, device_index)

                # This is the dendrites output after the nonlinearity was applied
                last_dendrite_outs = (
                    saved_values.dendrite_outs[device_index][-1]
                    .detach()
                    .clone()
                    .to(grad_out.device)
                )
                # In the current system this is the current error - the average error
                last_parent_d = (
                    saved_values.current_parent_d[device_index][-1]
                    .detach()
                    .clone()
                    .to(grad_out.device)
                )
                direction = saved_values.prev_dendrite_candidate_correlation.sign()
                reshape_direction = direction.view(view_tuple)
                # And here is the dendrite outs * (the current error - average error)
                # Dean/Charity, should this last_dendrite_outs - average dendrite out here)?
                # That should be top_dendrite_candidate_averages
                current_correlations = last_dendrite_outs * (last_parent_d)

                # looks like this is worse, but not sure why.  Switched back to the original and moveed on.
                # current_correlations = (last_dendrite_outs.to(last_parent_d.device)-aveOut) * (last_parent_d)
                # current_correlations = current_correlations.mean(math_tuple)

                # Future thought: can also try one where it switches to mean if the sum is > 1. or allow it to be set by layer manually
                # This is where you choose to use sum or mean for the correlations across the batch and convolution dimensions
                if GPA.pc.get_correlations_by_mean():
                    current_correlations = current_correlations.mean((math_tuple))
                else:
                    current_correlations = current_correlations.sum((math_tuple))

                # got rid of averagedsq because doing a proportional scaling later so this scaling doesnt matter.
                # I also dont think this was in the original cascor paper, though it was in the original implementation

                # Formula 0 is just the existing grad out times direction (val - average_d_matrix).
                # this is what I am currently using by default
                # Charity/Dean, Rethinking this now, this feels very very wrong.
                # I also thing it is wrong that I am doing sum/mean for n_error and d_output separately first and then
                # applying the multiplication after.  Think We definitely want to keep things separated until
                # we have covariance tensors and then do mean/sum at the end.
                if GPA.pc.get_formula_type() == 0:
                    grad_in = -(
                        grad_out.detach() * (reshape_direction)
                    )  # / ((saved_values.parents_average_d_sq + eps))
                # Formula 1 is trying to get the correlation multiplier back involved
                elif GPA.pc.get_formula_type() == 1:
                    grad_in = -(
                        grad_out.detach()
                        * current_correlations.view(view_tuple)
                        * (reshape_direction)
                    )  # / ((saved_values.parents_average_d_sq + eps))
                # This tries to devide by a factor that i think was introduced in original cascor
                elif GPA.pc.get_formula_type() == 2:
                    grad_in = -(
                        grad_out.detach()
                        * current_correlations.view(view_tuple)
                        * (reshape_direction)
                    )  # / ((saved_values.parents_average_d_sq + eps))
                    grad_in /= (
                        grad_out.pow(2) * current_correlations.view(view_tuple).pow(2)
                    ).sqrt()
                # This looks like it's doubling down on dendrite outs and not using correlation at all?  What was i thinking?
                elif GPA.pc.get_formula_type() == 3:
                    grad_in = -(
                        grad_out.detach()
                        * (
                            last_dendrite_outs
                            - saved_values.prev_dendrite_candidate_average.view(
                                view_tuple
                            )
                        )
                        * (reshape_direction)
                    )
                # same as above but with division step
                elif GPA.pc.get_formula_type() == 4:
                    grad_in = -(
                        grad_out.detach()
                        * (
                            last_dendrite_outs
                            - saved_values.prev_dendrite_candidate_average.view(
                                view_tuple
                            )
                        )
                        * (reshape_direction)
                    )
                    grad_in /= (
                        grad_out.pow(2)
                        * (
                            last_dendrite_outs
                            - saved_values.prev_dendrite_candidate_average.view(
                                view_tuple
                            )
                        ).pow(2)
                    ).sqrt()

                # Save the current candidate out as the last dendrite out
                saved_values.top_dendrite_candidate_averages.copy_(
                    last_dendrite_outs.mean((math_tuple))
                )
                # Update the running average of the candidate outs
                saved_values.prev_dendrite_candidate_average *= 0.99
                saved_values.prev_dendrite_candidate_average += (
                    saved_values.top_dendrite_candidate_averages * 0.01
                )

                if GPA.pc.get_extra_verbose():
                    print("new top")
                    print(saved_values.top_dendrite_candidate_averages)
                    print("new ave")
                    print(saved_values.prev_dendrite_candidate_average)
                    print("parentsAverageD")
                    print(saved_values.parents_average_d_vector)
                    print("last_dendrite_outs")
                    print(last_dendrite_outs)
                    print("last_parent_d")
                    print(last_parent_d)
                    print("current_correlations")
                    print(current_correlations)

                # this looks like im calculating correlation as (dendrite out * error) - (average out * average error)?
                # Dean/Charity, This definitely seems wrong, shoulnd't those pairings be flipped?
                cor = current_correlations - (
                    saved_values.prev_dendrite_candidate_average
                    * saved_values.parents_average_d_vector
                )  # / net['layers'][l]['sumSqError'][j]
                if GPA.pc.get_extra_verbose():
                    print("prev")
                    print(saved_values.prev_dendrite_candidate_correlation)
                    print("cor")
                    print(cor)
                    print("current_correlations")
                    print(current_correlations)
                # Update the running average of the correlations
                saved_values.prev_dendrite_candidate_correlation *= 0.99
                saved_values.prev_dendrite_candidate_correlation += cor * 0.01
                if GPA.pc.get_extra_verbose():
                    print("next prev")
                    print(saved_values.prev_dendrite_candidate_correlation)
                    if (
                        (saved_values.parents_average_d_vector).isnan().any()
                        or (saved_values.prev_dendrite_candidate_average).isnan().any()
                        or (saved_values.top_dendrite_candidate_averages).isnan().any()
                        or (current_correlations).isnan().any()
                    ):
                        print("got a nan in correlation score")
                        import pdb

                        pdb.set_trace()

                new_best_score, best_indices = new_best(saved_values)
                saved_values.best_score.copy_(new_best_score)

                beat_best = dendrite_score_beats_current_best(
                    saved_values.best_score, saved_values.previous_best_score
                )
                # If that best score has improved enough or this is the very first iteration
                if (beat_best) or saved_values.initialized.item() == 0:

                    if (
                        saved_values.best_score_improved_this_epoch[0] == 0
                        and GPA.pc.get_verbose()
                    ):
                        print(
                            "Score from %.16f to %.16f for %s with initialized %d"
                            % (
                                saved_values.previous_best_score.mean(),
                                saved_values.best_score.mean(),
                                saved_values.layer_name,
                                saved_values.initialized.item(),
                            )
                        )
                    # say that best score did improve this epoch and time step
                    saved_values.best_score_improved_this_epoch[0].copy_(
                        torch.tensor(1)
                    )
                    saved_values.best_score_improved_this_time_step[0].copy_(
                        torch.tensor(1)
                    )
                    # set the indexes of the best nodes
                    saved_values.indexes_of_best.copy_(best_indices)

                    ##check where temp_abs = best_score and save the weights for those candidates in forward for the layer next iteration
                    # this is where that saveBest function was maybe called?
                    # [values, indexes] = torch.max(saved_values.indexes_of_best, 0)
                    # TODO: this is supposed to be setting flags for which node indexes improved their max correlations
                    # But I'm not sure thats still whats happening 9.25.2025
                    saved_values.nodes_best_improved_this_epoch += (
                        saved_values.indexes_of_best
                    )
                    # only replace the ones that are bigger
                    saved_values.previous_best_score.copy_(
                        torch.max(
                            saved_values.best_score,
                            saved_values.previous_best_score,
                        ).detach()
                    )
                else:
                    # If dendrites did not improve their scores set that flag
                    saved_values.best_score_improved_this_time_step[0].copy_(
                        torch.tensor(0)
                    )
                    saved_values.indexes_of_best *= 0
                # This is just a debugging flag to let you check in on this function
                if saved_values.breaking.item():
                    pdb.set_trace()

                # TODO: 9.25.2025 what?? This looks like i am only updating averages if it is before the point of initialization?
                # that looks super wrong, its supposed to only be doing the averages differently before initialization
                # not skipping them entirely after initialization
                if (
                    saved_values.initialized.item()
                    < GPA.pc.get_initial_correlation_batches()
                ):
                    # Current correlations might not be required here if it is the same as above
                    update_saved_values_averages_initial(
                        saved_values,
                        current_correlations,
                        grad_in,
                        last_parent_d,
                        math_tuple,
                    )
                    # if its not initialized yet set scalar to 0 to weights dont get updated
                    scalar = 0.0000000
                else:
                    """
                    if this candidate is getting errors so low that the average at this point is 0
                    it is likely because vanishing gradient has died so theres not much to do here anyway
                    just set scalar to 0 and move on.  TODO: see if there is a better way to to this?
                    When it was caught with with autograd.detect_anomaly(): around forward->backward .normal_pass_average_d was actually
                    just a super small number but not exactly 0.
                    this means there is some amount of error it just is getting deleted after averaging because of float resolution.
                    TODO: not sure what benefit this was providing? could be removed?  was it a div0 error? 9.25.2025
                    """
                    if (
                        saved_values.candidate_grad_average_for_scaling.mean().item()
                        == 0
                    ):
                        # pdb.set_trace()
                        scalar = 0.0
                    else:
                        # saved_values.candidate_grad_average_for_scaling = grad_in.abs().mean(math_tuple) * 0.001 + saved_values.candidate_grad_average_for_scaling * 0.999
                        # grad_in = (grad_in * (saved_values.parents_average_d_vector.abs().mean()/saved_values.candidate_grad_average_for_scaling.abs().mean())) / saved_values.current_parent_d.abs().std()#.view(1,-1,1,1))
                        # scalar = saved_values.parents_average_d_vector.abs().mean()/saved_values.candidate_grad_average_for_scaling.abs().mean()

                        # Charity/Dean this is a scalar property I decided on after lots of just assorted experimnets.
                        # when you're checking the cascor math, I would reccomend just settint the scalar to 1
                        scalar = (
                            saved_values.main_grad_average_for_scaling.mean()
                            / saved_values.candidate_grad_average_for_scaling.mean()
                        )
                        # scalar = 1
                # doing thing defaults to false, but this also is just a scalar property I was experimenting with
                if GPA.pc.get_doing_thing():
                    scalar /= saved_values.parent_max_mean_act.item()
                # apply the scalar to the grad_in
                grad_in = grad_in * scalar
                # delete the current d and current outs from the saved values list
                del saved_values.current_parent_d[device_index][-1]
                del saved_values.dendrite_outs[device_index][-1]
                if GPA.pc.get_extra_verbose():
                    print("%s completing Dendrite backward" % saved_values.layer_name)

                return grad_in, None

    return Tagger.apply(inp)


def grad_killer(inp):
    """
    Kills the gradient for the input tensor but keeps forward
    """

    class Killer(torch.autograd.Function):
        # Potentially add staticmethod back later, but this doesnt work in compiled version
        # @staticmethod
        def forward(ctx, inp):
            return inp

        # Potentially add staticmethod back later, but this doesnt work in compiled version
        # @staticmethod
        def backward(ctx, grad_out):
            return grad_out * 0, None

    return Killer.apply(inp)


def no_forward(inp):
    """
    Kills the forward for the output tensor but keeps backward (which is then replaced in our backwards hooks)
    """

    class no_forward(torch.autograd.Function):
        # Potentially add staticmethod back later, but this doesnt work in compiled version
        # @staticmethod
        def forward(ctx, inp):
            return inp * 0

        # Potentially add staticmethod back later, but this doesnt work in compiled version
        # @staticmethod
        def backward(ctx, grad_out):
            return grad_out

    return no_forward.apply(inp)


def reinitialize_for_pb(dendrite_module):
    """
    When filling from n mode to p mode this function reinitializes the dendrite module variables
    And copies over the accumulated averages so Cascor has access to them
    """
    for val_name in MPA.DENDRITE_REINIT_VALUES:
        if (not val_name in NON_LIVE_SKIP_VALUES) or GPA.pc.get_learn_dendrites_live():
            setattr(dendrite_module, val_name, getattr(dendrite_module, val_name) * 0)

    if GPA.pc.get_doing_thing():
        dendrite_module.parent_max_mean_act.copy_(
            dendrite_module.normal_pass_max_mean_act.detach().clone()
        )
        dendrite_module.parent_max_mean_act.requires_grad = False
    dendrite_module.parents_average_d_vector.copy_(
        dendrite_module.normal_pass_average_d.detach().clone()
    )
    dendrite_module.parents_average_d_vector.requires_grad = False
    # dendrite_module.parents_average_d_mags.copy_(dendrite_module.normal_pass_average_d_mags.double().detach().clone())
    # dendrite_module.parents_average_d_sq.copy_(dendrite_module.normal_pass_average_d_sq.double().mean().detach().clone())
    # dendrite_module.parents_average_d_sq.requires_grad = False
    # dendrite_module.parents_average_d_mags.requires_grad = False
