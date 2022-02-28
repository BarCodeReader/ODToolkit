Feature: ObjectDetectionToolkit.Analysis.get_fpfn.feature

  Scenario Outline: test Analysis.get_fpfn behaviour
     Given image height "<height>" and width "<width>"
      When we pass gt labels at "<gt_lbl>" and pred labels at "<pred_lbl>" with iou_threshold "<iou_t>"
      Then the outcome should match pre-calculated "<answer>"
    Examples:
      |gt_lbl                         |pred_lbl                         |height| width| iou_t| answer                          |
      |./unit_tests/fixtures/gt/*.txt |./unit_tests/fixtures/pred/*.txt | 480  | 640  |  0.25| unit_tests/fixtures/answer.npy  |
