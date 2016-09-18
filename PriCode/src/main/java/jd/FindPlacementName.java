package jd;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Map;

/**
 * Created by tanzhen on 2016/6/1.
 * 根据推荐位ID 来查找推荐位名字
 */
public class FindPlacementName {
    static String pidFile_path = "C:\\Users\\Administrator\\Desktop\\pid.txt";
    static Map<String,WikiEntity> wikiEntityMap = null;

    public static void main(String[] args) throws Exception {
        wikiEntityMap = FilterUMPLatency.getWikiData(FilterUMPLatency.WikiFilePath);
        BufferedReader br = new BufferedReader(new FileReader(new File(pidFile_path)));
        String line = null;
        while ((line = br.readLine()) != null){
            if(wikiEntityMap.get(line) == null){
                System.out.println(line);
                continue;
            }
            String p_name = wikiEntityMap.get(line).p_name;
            String p_owner = wikiEntityMap.get(line).p_owner;
            System.out.println(line + "\t" + p_name + "\t" + p_owner);
        }
    }
}
