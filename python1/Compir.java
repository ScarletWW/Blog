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
 
public class Compir {
	private final String[] keyword = {""} 
		
		public static String readText(String filepath)//读取指定文件路径中的内容并将内容存到字符串中
		{
			String sentence1="";  
			try{  //读取test.txt文本中的内容，并保存在sentence1的字符流中。
			    BufferedReader str1=new BufferedReader(new FileReader(filepath));
			//"/Users/wanghaotian/Documents/c.txt"
					String line;
					while((line=str1.readLine())!=null) sentence1=sentence1+line+'\n';
				 	//System.out.println(sentence1);
				str1.close();	
				}
			catch(IOException e)
			{
				 e.printStackTrace();
			}
			return sentence1;
		}

		@Override
		public void run(String iFile, String oFile) throws IOException {
			// TODO Auto-generated method stub
			String sentence1 = readText(iFile);
			//writeText(sentence1, "test.txt");
			
		}
}