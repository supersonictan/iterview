package jd;

import java.io.*;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by tanzhen on 2016/4/29.
 * 根据UMP导出的Excel表，将其过滤为只有推荐位。
 *
 */
public class FilterUMPLatency {
    public static final String SOURCE_PATH = "D:\\a.csv";
    public static final String TARGET_PATH = "D:\\result.txt";
    public static final String WikiFilePath = "D:\\wiki.txt";


    public static void main(String[] args) throws Exception {
        System.out.println("确认已将ump导出的Excel表转为csv格式！");
        getUmpLatency("D:\\a.csv", "D:\\result.txt");
    }

    public static void getUmpLatency(String sourcePath, String targetPath) throws Exception {
        BufferedReader br = new BufferedReader(new FileReader(new File(sourcePath)));
        BufferedWriter bw = new BufferedWriter(new FileWriter(new File(targetPath)));
        Map<String,WikiEntity> wikiMap = getWikiData(WikiFilePath);

        bw.write("PID" + "\t" + "TP99" + "\t" + "TP999" + "\t" + "调用次数" + "\t" + "可用率" + "\t" + "名称" + "\t" + "位置" + "\t" + "Owner" + "\t" + "平台" + "\n");
        String line = null;
        while((line = br.readLine()) != null){

            String[] all = line.split(",");
            if(line.contains("result") || line.contains("full") || all[0].split("\\.").length != 2){
                continue;
            }
            String key = all[0];
            String Tp999 = all[6];
            String Tp99 = all[5];
            String callTime = all[10];
            String rate = all[11];
            String pid = key.split("\\.")[1].trim();
            String owner = null;
            String pname = null;
            String channel = null;
            String position = null;
            if(wikiMap.get(pid) != null){
                owner = wikiMap.get(pid).p_owner;
                pname = wikiMap.get(pid).p_name;
                channel = wikiMap.get(pid).channel;
                position = wikiMap.get(pid).position;
            }else {
                System.out.println("没有找到推荐位："+pid+" 在wiki中的信息");
            }

            bw.write(key + "\t" + Tp99 + "\t" + Tp999 + "\t" + callTime + "\t" + rate + "\t" + pname + "\t" + position + "\t" + owner + "\t" + channel + "\n");
        }
        bw.flush();
    }

    public static Map<String,WikiEntity> getWikiData(String wikiSourceFile) throws Exception {
        BufferedReader br = new BufferedReader(new FileReader(new File(wikiSourceFile)));
        Map<String,WikiEntity> wikiMap = new HashMap<String, WikiEntity>();
        String line = null;
        while ((line = br.readLine()) != null){
            String[] datas = line.split("\\|");
            String pid =datas[0].trim();
            String p_name =datas[1].trim();
            String p_position =datas[2].trim();
            String p_owner = datas[3].trim();
            String p_channel = datas[4].trim();

            WikiEntity entity = new WikiEntity(pid, p_name, p_owner,p_channel,p_position);
            System.out.println(entity);
            wikiMap.put(pid, entity);
        }
        br.close();
        return wikiMap;
    }
}

class WikiEntity{
    public String pid;
    public String p_name;
    public String p_owner;
    public String channel;
    public String position;

    public WikiEntity(String pid, String p_name, String p_owner, String channel, String position) {
        this.pid = pid;
        this.p_name = p_name;
        this.p_owner = p_owner;
        this.channel = channel;
        this.position = position;
    }

    @Override
    public String toString() {
        return "WikiEntity{" +
                "pid='" + pid + '\'' +
                ", p_name='" + p_name + '\'' +
                ", p_owner='" + p_owner + '\'' +
                ", channel='" + channel + '\'' +
                ", position='" + position + '\'' +
                '}';
    }
}
