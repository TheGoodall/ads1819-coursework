def count_ephemeral(n1, n2, k):
    k_eternal = set()
    k_ephemeral = set()
    count = 0

    def k_child(n):
        total = 0
        while n:
            n, digit = divmod(n, 10)
            total += digit ** k
        return total


    def determine_type(n):   #return True if ephermeral else return false
        visited = set()
        while 1:
            if n == 1:
                for number in visited:
                    k_ephemeral.add(number)
                return True
            elif n in k_ephemeral:
                for number in visited:
                    k_ephemeral.add(number)
                return True
            elif n in k_eternal:
                for number in visited:
                    if number not in k_eternal:
                        k_eternal.add(number)
                return False

            elif n in visited:
                for number in visited:
                    if number not in k_eternal:
                        k_eternal.add(number)
                return False

            else:
                visited.add(n)
                n = k_child(n)
                continue
    for i in range(n1, n2):
        if determine_type(i) == True:
            count += 1
    return count
    
print(count_ephemeral(1, 10000000, 4))
