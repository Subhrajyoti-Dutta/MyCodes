class Animal{
    void eatSomething(){
        System.out.println("eating something");
    }
}

class Dog extends Animal{
    void eatSomething() {
        System.out.println("Eating Pedigree");
    }
}

public class test_class2{
    float bmi;
    test_class2(int height, int weight){
        bmi=weight/height;
    }
    float BMI(){
        return bmi;
    }

    public static void main(String args[]){
        test_class2 s = new test_class2(154,64);
        System.out.println(s.BMI());
    }
}