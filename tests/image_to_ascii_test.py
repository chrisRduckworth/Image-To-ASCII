from image_to_ascii import get_subarray
import numpy as np

class TestGetSubarray:
    def test_returns_same_datatype(self):
        img = np.ones((5,5), np.bool_)
        img_2 = np.ones((5,5), np.float_)
        img_3 = np.ones((5,5), np.int_)

        imgs = [img, img_2, img_3]

        subs = [get_subarray(i, (1,1),  (2,2)) for i in imgs]

        assert all(subs[i].dtype == imgs[i].dtype for i in range(3))
        
    def test_returns_subarray_with_correct_dimensions(self):
        img = np.ones((5,5), np.bool_)

        for y in range(1, 5):
            for x in range(1, 5):
                sub = get_subarray(img, (0,0), (x,y))
                assert sub.shape == (y,x)

    def test_returns_subarray_starting_at_correct_position(self):
        img = np.random.rand(5,5)
        
        sub = get_subarray(img, (3,1), (2,3))
        for y in range(5):
            for x in range(5):
                sub = get_subarray(img, (x, y), (2,3))
                assert sub[0][0] == img[y][x]
    
    def test_returns_correct_subarray(self):
        img = np.fromfunction(lambda x,y: x + y, (5,5))
        expected = np.array([[2,3],[3,4],[4,5]])
        
        sub = get_subarray(img, (1,1), (2,3))

        assert np.array_equal(sub, expected)

    def test_pads_side_if_not_wide_enough(self):
        img = np.ones((5,5), dtype = np.bool_)
        expected = [[1,1,0,0] for i in range(4)]
        expected = np.array(expected, dtype = np.bool_)
        
        sub = get_subarray(img, (3,0), (4,4))

        assert np.array_equal(sub, expected)
