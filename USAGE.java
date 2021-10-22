import semantics.Compare;
import java.io.*;

public class USAGE {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
/*	
String a = "To simulate the behaviour of portions of the desired software product.";
String b = "High risk problems are address in the prototype program to make sure that the program is feasible.  A prototype may also be used to show a company that the software can be possibly programmed. ";
String c = "To simulate portions of the desired final product with a quick and easy program that does a small specific job.  It is a way to help see what the problem is and how you may solve it in the final project. ";
String d = "A prototype program simulates the behaviors of portions of the desired software product to allow for error checking. ";
String e = "Defined in the Specification phase a prototype stimulates the behavior of portions of the desired software product.  Meaning, the role of a prototype is a temporary solution until the program itself is refined to be used extensively in problem solving. ";
String f = "It is used to let the users have a first idea of the completed program and allow the clients to evaluate the program.  This can generate much feedback including software specifications and project estimations of the total project. ";
String g = "To find problem and errors in a program before it is finalized ";
String h = "To address major issues in the creation of the program.  There is no way to account for all possible bugs in the program, but it is possible to prove the program is tangible. ";
String i = "you can break the whole program into prototype programs to simulate parts of the final program. ";
String j = "To provide an example or model of how the finished program should perfom.  Provides forsight of some of the challanges that would be encountered.  Provides opportunity To introduce changes To the finished program. ";

*/
//System.out.println("Your first argument is: "+args[0]);  
String[] s = args[0].split("#");
String a = s[0].replace('@', ' ');
String b = s[1].replace('@', ' ');
//System.out.println(a+"---$$$$$$$$----"+b);
//System.out.println("\n\n\n");
Compare x = new Compare(a, b);
//System.out.println(a+"\n\n@@@@@@@@@@@@@@@@@@@@@@@@@");
//System.out.println("Similarity between the sentences : "+a+"\n-"+b+"\n is: " + x.getResult());
System.out.println( x.getResult());
/*
x = new Compare(a,c);
System.out.println("Similarity between the sentences : "+a+"\n-"+c+"\n is: " + x.getResult());

x = new Compare(a,d);
System.out.println("Similarity between the sentences : "+a+"\n-"+d+"\n is: " + x.getResult());

x = new Compare(a,e);
System.out.println("Similarity between the sentences : "+a+"\n-"+e+"\n is: " + x.getResult());

x = new Compare(a,f);
System.out.println("Similarity between the sentences : "+a+"\n-"+f+"\n is: " + x.getResult());

x = new Compare(a,g);
System.out.println("Similarity between the sentences : "+a+"\n-"+g+"\n is: " + x.getResult());

x = new Compare(a,h);
System.out.println("Similarity between the sentences : "+a+"\n-"+h+"\n is: " + x.getResult());

x = new Compare(a,i);
System.out.println("Similarity between the sentences : "+a+"\n-"+i+"\n is: " + x.getResult());

x = new Compare(a,j);
System.out.println("Similarity between the sentences : "+a+"\n-"+j+"\n is: " + x.getResult());
*/
	}

}
