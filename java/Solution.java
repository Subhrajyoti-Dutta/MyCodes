class Solution {
    public static boolean canBeValid(String s, String locked) {
        if (s.length() % 2 == 1)
            return false;
        int numOfBraket = 0;
        int leftBrac = 0;
        int rightBrac = 0;
        int i = 0;
        int changableLeftBrac = 0;
        int noneChangableLeftBrac = 0;
        for (int ind = 0; ind < s.length();ind++) {
            char c = s.charAt(ind);
            if (c == ')') {
                // System.out.println("if");
                if (numOfBraket > 0){
                    // System.out.println("\tif");
                    if (noneChangableLeftBrac > 0) {
                        noneChangableLeftBrac--;
                    } else {
                        changableLeftBrac--;
                    }
                    numOfBraket--;
                    ++leftBrac;
                }
                else if (locked.charAt(ind) == '0'){
                    // System.out.println("\telif");
                    numOfBraket++;
                    ++rightBrac;
                }
                else{
                    // System.out.println("\telse");
                    return false;
                }
            }
            else {
                // System.out.println("else");
                ++leftBrac;
                if (locked.charAt(ind) == '0'){
                    // System.out.println("\tif");
                    changableLeftBrac++;
                } else {
                    noneChangableLeftBrac++;
                }
                numOfBraket++;
                ++i;
            }
            System.out.print("index = ");
            System.out.print(ind);
            System.out.print(" numOfBraket = ");
            System.out.print(numOfBraket);
            System.out.print(" changableLeftBrac = ");
            System.out.println(changableLeftBrac);

        }
        if (numOfBraket != 0 && numOfBraket / 2 > changableLeftBrac){
            System.out.print(changableLeftBrac);
            return false;
        }

        return true;
    }
    
    public static void main(String[] args){
        System.out.println(canBeValid(
            "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(",
            "100011110110011011010111100111011101111110000101001101001111"
          // 012345678901234567890123456789012345678901234567890123456789
            ));
    }
}