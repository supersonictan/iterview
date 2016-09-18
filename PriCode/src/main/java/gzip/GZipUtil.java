package gzip;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.zip.GZIPInputStream;
import java.util.zip.GZIPOutputStream;

/**
 * Created by tanzhen on 2016/7/12.
 */
public class GZipUtil {

    public static String defaultEncode = "utf-8";

    public static byte[] toGZIPBytes(String str, String encoding){
        if(str == null || str.length() == 0){
            return null;
        }
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        GZIPOutputStream gzip = null;
        try {
            gzip = new GZIPOutputStream(out);
            gzip.write(str.getBytes(encoding));

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if(gzip != null){
                    gzip.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return out.toByteArray();
    }

    public static byte[] toGZIPBytes(String str){
        if(str == null || str.length() == 0){
            return null;
        }
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        GZIPOutputStream gzip = null;
        try {
            gzip = new GZIPOutputStream(out);
            gzip.write(str.getBytes(defaultEncode));

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if(gzip != null){
                    gzip.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return out.toByteArray();
    }

    public static String getFromGZip(byte[] bytes){
        if (bytes == null || bytes.length == 0) {
            return null;
        }
        String returnStr = null;
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        ByteArrayInputStream in = new ByteArrayInputStream(bytes);
        GZIPInputStream gunzip = null;
        try {
            gunzip = new GZIPInputStream(in);
            byte[] buffer = new byte[1];
            int n;
            while ((n = gunzip.read(buffer)) >= 0) {
                out.write(buffer, 0, n);
            }
            returnStr =  out.toString();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if(gunzip != null){
                    gunzip.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return returnStr;
    }
    public static String getFromGZip(byte[] bytes, String encoding){
        if (bytes == null || bytes.length == 0) {
            return null;
        }
        String returnStr = null;
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        ByteArrayInputStream in = new ByteArrayInputStream(bytes);
        GZIPInputStream gunzip = null;
        try {
            gunzip = new GZIPInputStream(in);
            byte[] buffer = new byte[1];
            int n;
            while ((n = gunzip.read(buffer)) >= 0) {
                out.write(buffer, 0, n);
            }
            returnStr =  out.toString(encoding);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if(gunzip != null){
                    gunzip.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return returnStr;
    }

    public static void main(String[] args) {
        String ss = "ssssssssssssssssssss111111111111111111111111111111111111111111112132sdffffffffffffffffffffffffffffffffffffffffff234sssss";
        System.out.println("len1:" + ss.getBytes().length);
        byte[] b = toGZIPBytes(ss);
        String sss = b.toString();
        System.out.println("len2:" + b.length);
        System.out.println(getFromGZip(sss.getBytes()));
    }
}
