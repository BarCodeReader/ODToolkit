Feature: ObjectDetectionToolkit.Visualization.show_boxes.feature

  Scenario Outline: test show box behaviour
     Given ODT BoxVisualizer with image height "<height>" and width "<width>"
      When we pass labels at "<labels>" and mode "<mode>"
      Then it should give not give any exceptions
    Examples:
      | labels                 | mode               | height | width |
      | 'unit_tests/fixtures'  | 'train'            | 480    | 640   |

