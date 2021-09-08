# Example program from https://github.com/squillero/python-accelerated
# Copyright © 2021 Giovanni Squillero <squillero@polito.it>
# Free for personal or classroom use; see 'LICENCE.md' for details.

# Find the list of all pairs those sum is 1,000, without duplicates (don't consider order).

data = [
    995, 967, 600, 464, 300, 846, 208, 210, 716, 989, 473, 810, 372, 42, 857, 829, 593, 588, 228,
    297, 955, 98, 869, 246, 233, 670, 539, 827, 587, 202, 358, 885, 860, 665, 539, 899, 161, 894,
    394, 512, 204, 676, 439, 345, 822, 992, 519, 109, 142, 325, 877, 623, 384, 936, 54, 654, 38,
    837, 386, 765, 47, 98, 965, 536, 326, 906, 768, 333, 954, 803, 605, 725, 306, 791, 629, 440,
    517, 679, 946, 782, 308, 48, 665, 209, 722, 164, 280, 240, 289, 983, 760, 134, 125, 263, 990,
    484, 180, 385, 549, 293, 717, 38, 502, 847, 958, 225, 347, 72, 112, 303, 151, 559, 246, 287,
    242, 19, 735, 508, 742, 575, 937, 807, 155, 612, 233, 98, 238, 335, 806, 749, 763, 293, 942,
    838, 481, 358, 39, 496, 308, 825, 772, 235, 674, 892, 186, 81, 723, 318, 385, 231, 386, 816,
    672, 222, 251, 123, 811, 908, 750, 382, 526, 609, 740, 350, 356, 24, 977, 793, 159, 836, 253,
    716, 676, 524, 774, 914, 986, 598, 460, 962, 471, 19, 671, 106, 588, 579, 239, 176, 661, 672,
    768, 484, 742, 429, 561, 477, 648, 305, 71, 52, 404, 159, 389, 942, 58, 320, 589, 529, 672, 552,
    684, 663, 979, 529, 277, 278, 219, 973, 719, 77, 644, 138, 42, 747, 104, 450, 820, 100, 60, 621,
    961, 94, 348, 299, 354, 747, 273, 549, 962, 641, 793, 926, 645, 316, 892, 270, 981, 358, 199,
    671, 293, 532, 483, 702, 532, 391, 316, 292, 184, 783, 7, 89, 905, 248, 443, 561, 935, 33, 578,
    768, 522, 98, 122, 638, 972, 94, 25, 630, 267, 525, 239, 230, 250, 250, 425, 567, 5, 538, 723,
    997, 392, 77, 821, 814, 488, 120, 81, 944, 347, 280, 303, 453, 598, 341, 283, 432, 128, 765,
    926, 157, 400, 617, 543, 278, 207, 75, 379, 981, 679, 44, 153, 834, 106, 592, 681, 436, 117,
    471, 174, 710, 380, 977, 658, 564, 724, 571, 856, 795, 202, 293, 325, 692, 9, 148, 416, 462, 93,
    135, 86, 228, 130, 331, 264, 215, 145, 282, 249, 751, 893, 798, 630, 69, 247, 676, 248, 273,
    967, 422, 392, 610, 325, 781, 918, 423, 533, 747, 517, 287, 821, 977, 253, 910, 358, 352, 833,
    861, 513, 430, 163, 997, 981, 444, 699, 607, 196, 481, 178, 763, 507, 642, 992, 237, 625, 334,
    251, 579, 450, 220, 663, 954, 617, 139, 762, 111, 120, 308, 252, 942, 818, 619, 500, 180, 915,
    678, 39, 552, 32, 728, 263, 985, 707, 455, 471, 182, 922, 828, 320, 662, 18, 274, 764, 474, 721,
    568, 932, 149, 706, 589, 855, 410, 509, 793, 190, 196, 938, 827, 848, 457, 857, 24, 213, 88,
    933, 513, 993, 443, 79, 467, 635, 608, 563, 304, 439, 194, 96, 831, 258, 244, 342, 235, 594,
    268, 740, 236, 916, 743, 742, 880, 903, 142, 357, 683, 95, 595, 151, 687, 638, 170, 970, 445,
    879, 174, 424, 252, 842, 49, 87, 405, 199, 534, 556, 196, 442, 848, 426, 167, 999, 312, 73, 630,
    217, 776, 513, 844, 401, 431, 947, 896, 865, 961, 105, 890, 443, 206, 906, 270, 559, 802, 658,
    554, 793, 963, 692, 99, 843, 213, 739, 403, 665, 574, 653, 565, 454, 217, 238, 941, 170, 506,
    189, 547, 445, 341, 272, 750, 174, 905, 812, 814, 509, 735, 220, 320, 242, 281, 41, 208, 406,
    119, 811, 530, 755, 372, 350, 917, 753, 82, 566, 261, 382, 490, 76, 16, 516, 371, 112, 605, 626,
    616, 29, 809, 946, 429, 367, 235, 658, 523, 580, 712, 701, 79, 587, 403, 108, 303, 944, 120,
    797, 119, 720, 723, 61, 207, 707, 126, 792, 702, 320, 815, 716, 166, 350, 842, 791, 976, 698,
    982, 870, 498, 706, 784, 268, 194, 136, 178, 286, 442, 441, 43, 834, 274, 808, 651, 836, 550,
    401, 635, 548, 135, 673, 503, 846, 755, 217, 590, 36, 792, 125, 549, 61, 54, 379, 129, 646, 131,
    895, 289, 632, 579, 963, 980, 991, 421, 281, 187, 149, 841, 695, 430, 540, 467, 114, 292, 816,
    312, 638, 279, 604, 763, 737, 601, 872, 709, 167, 550, 649, 163, 880, 807, 986, 599, 430, 363,
    390, 546, 200, 900, 351, 286, 630, 104, 236, 689, 280, 530, 987, 61, 594, 76, 687, 314, 606,
    543, 677, 620, 473, 18, 53, 376, 234, 862, 369, 52, 701, 208, 405, 658, 881, 1, 612, 674, 151,
    251, 517, 278, 452, 449, 791, 956, 905, 684, 315, 350, 19, 117, 43, 37, 680, 409, 20, 607, 14,
    249, 688, 208, 935, 21, 323, 456, 349, 561, 509, 500, 429, 351, 708, 193, 736, 908, 64, 137,
    928, 563, 964, 396, 600, 302, 940, 135, 902, 122, 482, 3, 405, 681, 949, 917, 437, 689, 524,
    216, 265, 389, 827, 532, 886, 616, 800, 318, 392, 498, 291, 197, 660, 720, 336, 234, 627, 256,
    16, 863, 939, 865, 628, 653, 636, 156, 617, 913, 642, 700, 958, 446, 453, 4, 2, 33, 6, 645, 944,
    196, 817, 743, 550, 560, 597, 437, 664, 824, 939, 10, 473, 655, 561, 355, 716, 633, 455, 364,
    648, 493, 266, 538, 185, 738, 415, 255, 410, 195, 32, 49, 466, 761, 878, 709, 526, 967, 450,
    520, 935, 116, 103, 158, 589, 343, 227, 231, 337, 565, 90, 688, 609, 681, 339, 799, 600, 972,
    846, 718, 745, 606, 363, 86, 988, 336, 977, 169, 794, 152, 461, 330, 859, 725, 665, 683, 84,
    956, 287, 979, 614, 985, 525, 339, 838, 841, 897, 966, 308, 976, 204, 360, 663, 680, 293, 907,
    422, 77, 712, 992, 688, 223, 358, 464, 362, 138, 493, 103, 886, 275, 383, 688, 79, 410, 31, 226,
    224, 788, 11, 935, 850, 203, 985, 344, 171, 801, 824, 478, 343, 160, 299, 894, 178, 743, 856,
    872, 827, 540, 935, 7, 370, 397, 147, 860, 391, 286, 350, 135, 991, 487, 110, 291
]

sum1000 = list()

# check (500, 500)
if data.count(500) > 1:
    sum1000.append((500, 500))

elem = set(data)
for e in elem:
    if e < 500 and 1000 - e in elem:
        sum1000.append((e, 1000 - e))

print(sorted(sum1000))
print(len(sum1000))