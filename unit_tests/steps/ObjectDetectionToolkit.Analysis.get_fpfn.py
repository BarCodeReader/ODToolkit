from behave import given, when, then
import sure
from ODToolkit.Analysis import get_fpfn
from PIL import Image
import numpy as np
import os
import glob


@given('image height "{height}" and width "{width}"')
def step_impl1(context, height, width):
    context.scenario.height = int(height)
    context.scenario.width = int(width)
    
@when('we pass gt labels at "{gt_lbl}" and pred labels at "{pred_lbl}" with iou_threshold "{iou_t}"')
def step_impl2(context, gt_lbl, pred_lbl, iou_t):
    context.scenario.gt_lbl = sorted(glob.glob(gt_lbl))
    context.scenario.pred_lbl = sorted(glob.glob(pred_lbl))
    context.scenario.iou_t = float(iou_t)

@then('the outcome should match pre-calculated "{answer}"')
def step_impl3(context, answer):
    fp, fn, correct = get_fpfn(gt_lbl=context.scenario.gt_lbl, 
                               pred_lbl=context.scenario.pred_lbl, 
                               iou_thresh=context.scenario.iou_t,
                               img_w=context.scenario.width,
                               img_h=context.scenario.height)
    context.scenario.answer = np.load(answer, allow_pickle=True)
    fp.should.equal(context.scenario.answer[0])
    fn.should.equal(context.scenario.answer[1])
    correct.should.equal(context.scenario.answer[2])
