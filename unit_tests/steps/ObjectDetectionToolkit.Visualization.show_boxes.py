from behave import given, when, then
import sure
from ODToolkit.Visualization import BoxVisualizer
from PIL import Image
import numpy as np
import os
import glob


@given('ODT BoxVisualizer with image height "{height}" and width "{width}"')
def step_impl1(context, height, width):
    context.scenario.box_visualizer = BoxVisualizer(img_h=int(height),
                                                    img_w=int(width))

@when('we pass labels at "{labels}" and mode "{mode}"')
def step_impl2(context, labels, mode):
    # convert image into resource
    context.scenario.labels = [glob.glob(labels+'/*.txt')]
    context.scenario.mode = [mode]

@then('it should give not give any exceptions')
def step_impl3(context):
    context.scenario.box_visualizer.show_boxes.when.called_with(
        labels=context.scenario.labels,
        mode=context.scenario.mode).should.be.ok