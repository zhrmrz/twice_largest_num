class Sol:
    def twice_largest_num(self,arr):
        maxi=max(arr)
        for num in arr:
            if num!=maxi:
                if num*2>maxi:
                    return False
        return True



if __name__ == '__main__':
    p=Sol()
    print(p.twice_largest_num([1, 2, 4]))
