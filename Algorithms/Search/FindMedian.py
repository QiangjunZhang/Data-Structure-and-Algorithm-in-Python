from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #find the final left median list length
        if len(nums1) < len(nums2):
            nums3 = nums2
            nums2 = nums1
            nums1 = nums3

        m = len(nums1)
        n = len(nums2)
        med = (m+n) // 2 + 1
        #find the correct contributing number of items from list1
        split = 1
        start = 0
        end = m
        mid = (end - start) // 2 + start
        while split:
            if n == 0:
                mid = med
                break
            if end - start == 1:
                mid += 1
            else:
                mid = (end - start)//2 + start
            if med - mid > n:
                start +=1
                continue
            if med - mid < 0:
                start -=1
                continue
            if med - mid < n:
                if nums1[mid - 1] > nums2[med-mid]:
                    end = mid
                    continue
            if med - mid > 0 and mid < m :
                if nums1[mid] < nums2[med-mid-1]:
                    start = mid
                    continue


            # if nums1[mid - 1] <= nums2[med-mid]:
            split = 0

        if (m+n) % 2 != 0:
            if med - mid == 0:
                mediant = nums1[mid - 1]
            elif nums1[mid - 1] <= nums2[med-mid-1]:
                mediant = nums2[med-mid-1]
            else:
                mediant = nums1[mid - 1]
        else:
            if med - mid == 0 :
                mediant = (nums1[mid - 1] + nums1[mid - 2]) / 2
                return mediant
            mediant = (nums1[mid - 1] + nums2[med - mid - 1]) / 2
            if med - mid > 1 and mid > 1:
                if nums1[mid - 1] < nums2[med-mid-2]:
                    mediant = (nums2[med-mid - 2] + nums2[med - mid - 1]) / 2
                if nums1[mid - 2] > nums2[med-mid-1]:
                    mediant = (nums1[mid - 2] + nums1[mid - 1]) / 2
            elif mid == 1:
                if med - mid > 1:
                    if nums1[mid - 1] < nums2[med - mid - 2]:
                        mediant = (nums2[med - mid - 2] + nums2[med - mid - 1]) / 2
            elif med - mid == 1:
                if nums1[mid - 2] > nums2[med-mid-1]:
                    mediant = (nums1[mid - 2] + nums1[mid - 1]) / 2
        return mediant


def main():
    x = Solution()
    nums1 = [7]
    nums2 = [1,2,3,4,5,6,8,9]
    mediant = x.findMedianSortedArrays(nums1,nums2)
    print(mediant)




def test():
    m = 5
    med = 6 // 2 + 1

    print(med)

if __name__ == '__main__':
    # test()
    main()