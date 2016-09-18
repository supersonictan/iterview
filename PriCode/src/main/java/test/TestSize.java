package test;

/**
 * Created by tanzhen on 2016/6/29.
 */
public class TestSize {

    static String pin = "我爱大连";
    static long timestamp = System.currentTimeMillis();
    static float weight = 1.123f;
    static long sku = 12345678L;
    static int featureSize = 350;
    static  int skuSize = 20;


    public static void main(String[] args) {
        String skuInfo = String.valueOf(sku) + ":";
        String weightInfo = "";
        for(int i=0; i<featureSize; i++){
            if(weightInfo.equals("") || weightInfo == null){
                weightInfo += weight;
            }else {
                weightInfo = weightInfo + "," + weight;
            }
        }
        String info = skuInfo + weightInfo;
        StringBuffer sb = new StringBuffer();
        for(int i=0;i<skuSize;i++){
            if(sb.length() == 0){
                sb.append("[").append(info).append("]");
            }else {
                sb.append(",[").append(info).append("]");
            }
        }
        String str = pin + "," + timestamp + "," +  sb.toString();
        System.out.println(str.getBytes().length/1024);
    }
}
