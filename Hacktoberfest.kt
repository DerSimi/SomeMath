import kotlin.math.cos

class Hacktoberfest {
    //for k = 5 the method prints 1 4 9 16 25
    fun generateNumbersWithAnNaturalNumberAsSquareRoot(k: Int): IntArray = if (k <= 0) IntArray(0) else {
        val array = IntArray(k)
        var sum = 0

        for (i in 0 until k) {
            sum += 2 * i + 1
            array[i] = sum
        }

        array
    }

    //0! = 0; 5! = 120, .... n! = n(n-1)! k>0
    fun fact(k: Int): Int = if (k == 1 || k == 0) 1 else k * fact(k - 1)

    //n>k and n,k>0
    fun binomialCoefficient(n: Int, k: Int) = fact(n) / (fact(k) * (fact(n - k)))

    fun cosineFixpoint(iterations: Int) = if (iterations <= 0) 0 else {
        var ans = 0.5

        for (i in 0..iterations)
            ans = cos(ans)

        ans
    }

    //TODO: create matrix object
    fun solveLinearSystem(
        a_11: Double,
        a_12: Double,
        a_21: Double,
        a_22: Double,
        b_1: Double,
        b_2: Double
    ): Pair<Double?, Double?> {//With two unknowns, no time for the general case. Special cases were not considered, the program returns no solution for a system like: 0x + py = q; kx + 0y = z
        val detM = a_11 * a_22 - a_21 * a_12

        return if (detM != 0.0) {
            Pair((b_1 * a_22 - b_2 * a_12) / detM, (a_11 * b_2 - a_21 * b_1) / detM)
        } else
            Pair(null, null)//Error
    }

}