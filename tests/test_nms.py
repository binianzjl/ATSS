# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

import unittest

import numpy as np
import torch
from atss_core.layers import nms as box_nms


class TestNMS(unittest.TestCase):
    def test_nms_cpu(self):
        """ Match unit test UtilsNMSTest.TestNMS in
            caffe2/operators/generate_proposals_op_util_nms_test.cc
        """

        inputs = (
            np.array(
                [
                    10,
                    10,
                    50,
                    60,
                    0.5,
                    11,
                    12,
                    48,
                    60,
                    0.7,
                    8,
                    9,
                    40,
                    50,
                    0.6,
                    100,
                    100,
                    150,
                    140,
                    0.9,
                    99,
                    110,
                    155,
                    139,
                    0.8,
                ]
            )
            .astype(np.float32)
            .reshape(-1, 5)
        )

        boxes = torch.from_numpy(inputs[:, :4])
        scores = torch.from_numpy(inputs[:, 4])
        test_thresh = [0.1, 0.3, 0.5, 0.8, 0.9]
        gt_indices = [[1, 3], [1, 3], [1, 3], [1, 2, 3, 4], [0, 1, 2, 3, 4]]

        for thresh, gt_index in zip(test_thresh, gt_indices):
            keep_indices = box_nms(boxes, scores, thresh)
            keep_indices = np.sort(keep_indices)
            np.testing.assert_array_equal(keep_indices, np.array(gt_index))

    def test_nms1_cpu(self):
        """ Match unit test UtilsNMSTest.TestNMS1 in
            caffe2/operators/generate_proposals_op_util_nms_test.cc
        """

        boxes = torch.from_numpy(
            np.array(
                [
                    [350.9821, 161.8200, 369.9685, 205.2372],
                    [250.5236, 154.2844, 274.1773, 204.9810],
                    [471.4920, 160.4118, 496.0094, 213.4244],
                    [352.0421, 164.5933, 366.4458, 205.9624],
                    [166.0765, 169.7707, 183.0102, 232.6606],
                    [252.3000, 183.1449, 269.6541, 210.6747],
                    [469.7862, 162.0192, 482.1673, 187.0053],
                    [168.4862, 174.2567, 181.7437, 232.9379],
                    [470.3290, 162.3442, 496.4272, 214.6296],
                    [251.0450, 155.5911, 272.2693, 203.3675],
                    [252.0326, 154.7950, 273.7404, 195.3671],
                    [351.7479, 161.9567, 370.6432, 204.3047],
                    [496.3306, 161.7157, 515.0573, 210.7200],
                    [471.0749, 162.6143, 485.3374, 207.3448],
                    [250.9745, 160.7633, 264.1924, 206.8350],
                    [470.4792, 169.0351, 487.1934, 220.2984],
                    [474.4227, 161.9546, 513.1018, 215.5193],
                    [251.9428, 184.1950, 262.6937, 207.6416],
                    [252.6623, 175.0252, 269.8806, 213.7584],
                    [260.9884, 157.0351, 288.3554, 206.6027],
                    [251.3629, 164.5101, 263.2179, 202.4203],
                    [471.8361, 190.8142, 485.6812, 220.8586],
                    [248.6243, 156.9628, 264.3355, 199.2767],
                    [495.1643, 158.0483, 512.6261, 184.4192],
                    [376.8718, 168.0144, 387.3584, 201.3210],
                    [122.9191, 160.7433, 172.5612, 231.3837],
                    [350.3857, 175.8806, 366.2500, 205.4329],
                    [115.2958, 162.7822, 161.9776, 229.6147],
                    [168.4375, 177.4041, 180.8028, 232.4551],
                    [169.7939, 184.4330, 181.4767, 232.1220],
                    [347.7536, 175.9356, 355.8637, 197.5586],
                    [495.5434, 164.6059, 516.4031, 207.7053],
                    [172.1216, 194.6033, 183.1217, 235.2653],
                    [264.2654, 181.5540, 288.4626, 214.0170],
                    [111.7971, 183.7748, 137.3745, 225.9724],
                    [253.4919, 186.3945, 280.8694, 210.0731],
                    [165.5334, 169.7344, 185.9159, 232.8514],
                    [348.3662, 184.5187, 354.9081, 201.4038],
                    [164.6562, 162.5724, 186.3108, 233.5010],
                    [113.2999, 186.8410, 135.8841, 219.7642],
                    [117.0282, 179.8009, 142.5375, 221.0736],
                    [462.1312, 161.1004, 495.3576, 217.2208],
                    [462.5800, 159.9310, 501.2937, 224.1655],
                    [503.5242, 170.0733, 518.3792, 209.0113],
                    [250.3658, 195.5925, 260.6523, 212.4679],
                    [108.8287, 163.6994, 146.3642, 229.7261],
                    [256.7617, 187.3123, 288.8407, 211.2013],
                    [161.2781, 167.4801, 186.3751, 232.7133],
                    [115.3760, 177.5859, 163.3512, 236.9660],
                    [248.9077, 188.0919, 264.8579, 207.9718],
                    [108.1349, 160.7851, 143.6370, 229.6243],
                    [465.0900, 156.7555, 490.3561, 213.5704],
                    [107.5338, 173.4323, 141.0704, 235.2910],
                ]
            ).astype(np.float32)
        )
        scores = torch.from_numpy(
            np.array(
                [
                    0.1919,
                    0.3293,
                    0.0860,
                    0.1600,
                    0.1885,
                    0.4297,
                    0.0974,
                    0.2711,
                    0.1483,
                    0.1173,
                    0.1034,
                    0.2915,
                    0.1993,
                    0.0677,
                    0.3217,
                    0.0966,
                    0.0526,
                    0.5675,
                    0.3130,
                    0.1592,
                    0.1353,
                    0.0634,
                    0.1557,
                    0.1512,
                    0.0699,
                    0.0545,
                    0.2692,
                    0.1143,
                    0.0572,
                    0.1990,
                    0.0558,
                    0.1500,
                    0.2214,
                    0.1878,
                    0.2501,
                    0.1343,
                    0.0809,
                    0.1266,
                    0.0743,
                    0.0896,
                    0.0781,
                    0.0983,
                    0.0557,
                    0.0623,
                    0.5808,
                    0.3090,
                    0.1050,
                    0.0524,
                    0.0513,
                    0.4501,
                    0.4167,
                    0.0623,
                    0.1749,
                ]
            ).astype(np.float32)
        )

        gt_indices = np.array(
            [
                1,
                6,
                7,
                8,
                11,
                12,
                13,
                14,
                17,
                18,
                19,
                21,
                23,
                24,
                25,
                26,
                30,
                32,
                33,
                34,
                35,
                37,
                43,
                44,
                47,
                50,
            ]
        )
        keep_indices = box_nms(boxes, scores, 0.5)
        keep_indices = np.sort(keep_indices)

        np.testing.assert_array_equal(keep_indices, gt_indices)


if __name__ == "__main__":
    unittest.main()
