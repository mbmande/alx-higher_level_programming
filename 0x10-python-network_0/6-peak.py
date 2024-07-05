#!/usr/bin/python3
"""
sgdsjdsjdsdkjldksdjk
"""

def find_peak(list_of_integers):
        size = len(list_of_integers)
            mid = size // 2

                if size == 0:
                            return None

                            while True:
                                        mid_e = size // 2
                                                if mid < size - 1 and list_of_integers[mid] < list_of_integers[mid + 1]:
                                                                mid = mid + mid_e // 2
                                                                        elif mid_e > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
                                                                                        mid = mid - mid_e // 2
                                                                                                else:
                                                                                                                return list_of_integers[mid]
