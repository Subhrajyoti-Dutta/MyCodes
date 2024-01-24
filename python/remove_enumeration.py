a = """1     public class Employee {
2            public void display( ){
3                   System.out.print("In Employee class");
4            }
5     }
6     public class TeamLead extends Employee{
7            public void display( ){
8                   System.out.println("In TeamLead class");
9            }
10    }
11    public class Manager extends Employee, TeamLead{
12           public void display( ){
13                 System.out.println("In Manager class");
14           }
15           public static void main(String[] arg) {
16                 TeamLead t = new Employee( );
17           }
18    }"""

a = "\n".join(map(lambda x : x[6:],a.split("\n")))

print(a)