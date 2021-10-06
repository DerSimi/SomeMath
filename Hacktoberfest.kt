class Hacktoberfest {
    //for k = 5 the method prints 1 4 9 16 25 36
    fun generateNumbersWithAnNaturalNumberAsSquareRoot(k: Int) : IntArray {
        var array = IntArray(k)

        if(k <= 0) return array

        var sum = 0
        var count = 0

        while(count < k) {
            sum += 2 * (count) + 1
            array[count] = sum

            count++
        }

        return array
    }
}