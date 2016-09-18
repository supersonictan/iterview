package jd;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by tanzhen on 2016/5/29.
 * 根据两个IP文件，找出不一样的（可以扩展到其他以行为单位的文本）
 * 若只输入一个文本，则检测文本是否有重复
 */
public class CompareIP {
    public static List<String> list_A = new ArrayList<String>();
    public static List<String> list_B = new ArrayList<String>();
    public static List<String> notExistInB = new ArrayList<String>();
    public static List<String> notExistInA = new ArrayList<String>();
    public static List<String> multi_in_A = new ArrayList<String>();


    public static void main(String[] args) {
        System.out.println("请将两个文本命名为 a.txt 和b.txt，并放于windows桌面");
        String fileA_Path = "C:\\Users\\Administrator\\Desktop\\a.txt";
        String fileB_Path = "C:\\Users\\Administrator\\Desktop\\b.txt";

        BufferedReader reader_A = null;
        BufferedReader reader_B = null;
        try {
            reader_A = new BufferedReader(new FileReader(new File(fileA_Path)));
            reader_B = new BufferedReader(new FileReader(new File(fileB_Path)));
            String line = null;
            while((line=reader_A.readLine()) != null){
                list_A.add(line);
            }
            while ((line = reader_B.readLine()) != null){
                list_B.add(line);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                reader_A.close();
                reader_B.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        /**
         * 任务：找到A中存在，但是B中不存在
         */
        for(String str_A : list_A){
            if(list_B.contains(str_A)){
                continue;
            }else {
                notExistInB.add(str_A);
            }
        }

        /**
         * 任务：找到B中存在，但是A中不存在
         */
        for(String str_B: list_B){
            if(list_A.contains(str_B)){
                continue;
            }else {
                notExistInA.add(str_B);
            }
        }

        System.out.println("如下文本A有，B无："+ notExistInB);
        System.out.println("如下文本B有，A无："+ notExistInA);

    }

}
