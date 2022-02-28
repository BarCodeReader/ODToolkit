from behave import given, when, then
import sure
from ODToolkit.Transformation import xy_to_homo, homo_to_xy
from PIL import Image
import numpy as np
import os
import glob


@given('homography matrix of "{homo}"')
def step_impl1(context, homo):
    context.scenario.homo = np.load(homo, allow_pickle=True)

# xy_to_homo function
@when('we pass xy coordinate of x "{x}" and y "{y}"')
def step_impl2(context, x, y):
    context.scenario.x_homo,  context.scenario.y_homo = xy_to_homo(int(x), int(y), context.scenario.homo)

@then('the transformed x_homo and y_homo should match pre-calculated "{x_homo}" and "{y_homo}"')
def step_impl3(context, x_homo, y_homo):

    context.scenario.x_homo.should.equal(int(x_homo))
    context.scenario.y_homo.should.equal(int(y_homo))

# homo_to_xy function
@when('we pass xy in homography coordinate of x_homo "{x_homo}" and y_homo "{y_homo}"')
def step_impl2(context, x_homo, y_homo):
    context.scenario.x,  context.scenario.y = homo_to_xy(int(x_homo), int(y_homo), context.scenario.homo)

@then('the transformed x and y should match pre-calculated "{x}" and "{y}"')
def step_impl3(context, x, y):

    context.scenario.x.should.equal(int(x))
    context.scenario.y.should.equal(int(y))
    
