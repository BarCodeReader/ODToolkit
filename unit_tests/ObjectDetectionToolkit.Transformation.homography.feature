Feature: ObjectDetectionToolkit.Transformation.homography.feature

  Scenario Outline: test Transformation.xy_to_homo behaviour
     Given homography matrix of "<homo>"
      When we pass xy coordinate of x "<x>" and y "<y>"
      Then the transformed x_homo and y_homo should match pre-calculated "<x_homo>" and "<y_homo>"
    Examples:
      |homo                          |  x  |  y | x_homo |y_homo|
      |./unit_tests/fixtures/homo.npy| 101 | 91 | 222    |  492 |
      |./unit_tests/fixtures/homo.npy|  59 | 34 | 124    |  359 |
      |./unit_tests/fixtures/homo.npy|  10 | 18 | 39     |  296 |

  Scenario Outline: test Transformation.homo_to_xy behaviour
     Given homography matrix of "<homo>"
      When we pass xy in homography coordinate of x_homo "<x_homo>" and y_homo "<y_homo>"
      Then the transformed x and y should match pre-calculated "<x>" and "<y>"
    Examples:
      |homo                          |  x  |  y | x_homo |y_homo|
      |./unit_tests/fixtures/homo.npy| 101 | 91 | 222    |  492 |
      |./unit_tests/fixtures/homo.npy|  59 | 34 | 124    |  359 |
      |./unit_tests/fixtures/homo.npy|  10 | 18 | 39     |  296 |
