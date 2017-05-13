import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter; 
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileOutputStream; 
import java.io.OutputStreamWriter; 
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.awt.print.*;

//首先定义一个结构体用来存储分离出的单词的内容、类型、行号
class Word{
     String value;//平台左端的位置
     String type;//平台右边的位置
     int line;//平台离地面的高度
    public String getValue() {
       // return value;
        System.out.print(value+" ");
        return value;
    }
    Word(String value,String type,int line) {
        this.value = value;
         this.type = type;
        this.line = line;
    }
    public String getType() {
        System.out.print(type+" ");
        return type;
    }
    public void setType(String type) {
        this.type = type;
    }
    public int getLine() {
        System.out.print(line);
        return line;
    }
    public void setH(int line) {
        this.line = line;
    }
}
// 
public class Comp { 

        public static Word[] wd = new Word[100];
        public static int k=0;
        public static char ch;
        public static StringBuffer strToken = new StringBuffer();//存放构成单词符号的字符串 
        private static String dyhStr = "'";  //,dyhStr.charAt(0)
        private static  String[] keyword = {"auto","if","unsigned","break","inline","void","case","int","volatile","char","long","while","const","register","continue","default","return","do","double","signed","else","sizeof","enum","static","extern","struct","float","switch","for","typedef","goto","union","_Alignas","_Alignof","_Atomic","_Bool","_Complex","_Generic","_Imaginary","_Noreturn","_Static_assert","_Thread_local","main"}; 
        private static char[] separator = { '+', '-', '*', '/', '=', '<', '>',  '(', ')', '[', ']', ':', '.', ';', ',', '&','!','{','}','%','^','|'};
        private static String[] separator2={"->","++","--","+=","<=",">=","!=","*=","/=","<:",":>","<%","%>","%:"};  
          
         // 判断是否为保留字，每次读取的是字符串  
        public static boolean isKeyWord(String str) 
        {  
            for (int i = 0; i < keyword.length; i++) {  
                if (keyword[i].equals(str)) {  
                    return true;  
                }  
        }  
        return false;  
        }
//        //判断是否是字母  
//        public boolean IsLetter(char ch){  
//            if((ch>='a' && ch <= 'z') || (ch >= 'A' && ch <='Z')){  
//                return true;  
//            }  
//            return false;  
//        }  
        //判断是否是空格  
        public static boolean IsBC(char ch){  
            if(ch == ' '){  
                return true;  
            }  
            return false;  
        }  
        // 判断是否是数字，每次读取的是字符  
        public static boolean isDigit(char ch) 
        {  
            if (ch >= 48 && ch <= 57) {  
                return true;  
            }   else {  
            return false;  
            }  
        }  
  
        // 判断是否为字母，每次读取的是字符  
        public static boolean isLetter(char ch) {  
            if ((ch >= 65 && ch <= 90) || (ch >= 97 && ch <= 122) | (ch == 37)) {  
                return true;  
            } else {  
                return false;  
            }  
        }
        //判断是否是分隔符，有单字符和双字符的分隔符
        public static boolean isSeparator(char ch) {  
        for (int i = 0; i < separator.length; i++) {  
            if (separator[i]==ch) {  
                return true;  
            }  
        }  
        return false;  
        }
        public static boolean isSeparator2(String ch) {  
            for (int i = 0; i < separator2.length; i++) {  
                if (ch.toString().equals(separator2[i])) {  
                    return true;  
                }  
            }  
            return false;  
            }

        //下面是分析的主程序，从头开始扫描每一行，
        public static void tokenAnysis (String str)
        {
            String sentence1 =str;
            int line=1;
            //System.out.println(sentence1.length());
            for(int i=0;i<sentence1.length();i++)
            {
                ch=sentence1.charAt(i);
                //System.out.print(ch);
                if(IsBC(ch)==true)
                {
                    
                    strToken.delete(0, strToken.length()); 
                    //i++;
                   
                    continue; 
                }
                if(ch=='\n')
                {
                    line++;
                }
                //如果是分隔符，判断接下来的两个字符，直到不是分割符
                if(isSeparator(ch)==true)
                {
                    
                    
                    strToken.append(ch);
                    //System.out.println(sentence1.charAt(i+1));
                    if ((i+1)<sentence1.length()&&isSeparator(sentence1.charAt(i+1))) {
                        strToken.append(sentence1.charAt(i+1));
                        if(isSeparator2(strToken.toString()))
                        {
                            wd[k++]=new Word(strToken.toString(),"separator",line);
                           
                            i=i+1;
                       
                        }
                        else{
                            System.out.println("Wrong Separator!\n");
                            System.exit(0);
                        }
                    }
                    else {
                        wd[k++]=new Word(strToken.toString(),"separator",line);
                        
                    }
                    
                                        
                }
                //如果这个字符是字母，那么继续向下查找，直到找到非字母和数字
                if (isLetter(ch)) {
                    //strToken.append(ch);
                    int j=0;
                    for( j=0;j<sentence1.length()-i;j++)
                    {
                        if(isDigit(sentence1.charAt(i+j)) || isLetter(sentence1.charAt(i+j)))
                        {
                            strToken.append(sentence1.charAt(i+j));
                        }
                        else{
                            break;
                        }
                    }
                    if(isKeyWord(strToken.toString())==true)
                    {
                        wd[k++]=new Word(strToken.toString(),"keyword",line);
                        i=i+j-1;
                    }
                    else{
                        wd[k++]=new Word(strToken.toString(),"identifier",line);
                        i=i+j-1;
                    }
                }
                if(isDigit(ch))
                {
                    int j=0;
                    for( j=0;j<sentence1.length()-i;j++)
                    {
                        if(isDigit(sentence1.charAt(i+j)))
                        {
                            strToken.append(sentence1.charAt(i+j));
                        }
                        else{
                            break;
                        }
                    }
                    wd[k++]=new Word(strToken.toString(),"const_i",line);
                    i=i+j-1;

                }
                if(ch=='"')
                {
                    int j=0;
                    strToken.append('"');
                    for( j=1;j<sentence1.length()-i;j++)
                    {
                        if(sentence1.charAt(i+j)==ch)
                        {
                            strToken.append(sentence1.charAt(i+j));
                            //System.out.println("2222");
                            break;
                        }
                        else {
                            strToken.append(sentence1.charAt(i+j));
                        }
                        
                    }
                    wd[k++]=new Word(strToken.toString(),"stringLiteral",line);
                    i=i+j;

                    //System.out.println("1111");
                }
                
                strToken.delete(0, strToken.length());
                
            }
            
        }
        public static String readText(String filepath)//读取指定文件路径中的内容并将内容存到字符串中
        {
            String sentence1="";  
            try{  //读取test.txt文本中的内容，并保存在sentence1的字符流中。
                BufferedReader str1=new BufferedReader(new FileReader(filepath));
            //"/Users/wanghaotian/Documents/c.txt"
                    String line;
                    while((line=str1.readLine())!=null) sentence1=sentence1+line+"\n";
                    //System.out.println(sentence1);
                str1.close();   
                }
            catch(IOException e)
            {
                 e.printStackTrace();
            }
            return sentence1;
        }
        public static void main(String[] args) {  
            String str1=readText("test.txt");
            Comp compile2 = new Comp();  
            compile2.tokenAnysis(str1); 
            
            for (int i=0;i<k;i++) {
                wd[i].getValue();
                wd[i].getType();
                wd[i].getLine();
                System.out.println("\n");
            } 
            //String str1=readText("test.txt");
            //System.out.println(str1);
        }  

//        @Override
//        public void run(String iFile, String oFile) throws IOException {
//            // TODO Auto-generated method stub
//            //String sentence1 = readText(iFile);
//            //writeText(sentence1, "test.txt");
//            tokenAnysis
//            
//        }
}