class Hacktoberfest {
    //for k = 5 the method prints 1 4 9 16 25
    fun generateNumbersWithAnNaturalNumberAsSquareRoot(k: Int) : IntArray {
        val array = IntArray(k)

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

    //0! = 0; 5! = 120, .... n! = n(n-1)! k>0
    fun fact(k: Int) : Int = if(k == 1 || k == 0) 1 else k * fact(k - 1)

    //n>k and n,k>0
    fun binomialCoefficient(n: Int, k: Int) = fact(n) / (fact(k)*(fact(n-k)))
}