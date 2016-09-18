/*
package httpClient;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.ByteArrayEntity;
import org.apache.http.util.EntityUtils;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.Map;

*/
/**
 * Created by tanzhen on 2016/7/12.
 *//*

public class HttpClientUtils {


    private static final String UTF_8 = "UTF-8";
    private static final String HEADER_CHARSET = "Accept-Charset";
    private static final String HEADER_CONTENT_TYPE = "Content-Type";
    private static final String JSON_UTF8 = "application/json; charset=utf-8";


    public static ByteArrayEntity byteArrayEntity(String content) {
        if(content == null || "".equals(content)){
            return null;
        }
        try {
            return new ByteArrayEntity(content.getBytes(UTF_8));
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        return null;
    }


    public static String post(String url, Map<String, String> headers, HttpEntity httpEntity, int socketTimeout, int connectTimeout, int connectRequestTimeout, boolean compression) {
        RequestConfig requestConfig = RequestConfig.copy(RequestConfig.DEFAULT)
                .setSocketTimeout(socketTimeout)
                .setConnectTimeout(connectTimeout)
                .setConnectionRequestTimeout(connectRequestTimeout)
                .setContentCompressionEnabled(compression)
                .build();

        final HttpEntity entity;
        if (compression && httpEntity != null) {
            entity = new GzipCompressingEntity(httpEntity);
        } else {
            entity = httpEntity;
        }

        HttpPost post = new HttpPost(url);
        post.setConfig(requestConfig);
        post.setHeader(HEADER_CHARSET, UTF_8);
        post.setHeader(HEADER_CONTENT_TYPE, JSON_UTF8);
        //post.setHeader(HEADER_DATE, String.valueOf(System.currentTimeMillis()));
        if (headers != null && !headers.isEmpty()) {
            for (Map.Entry<String, String> entry : headers.entrySet()) {
                post.setHeader(entry.getKey(), entry.getValue());
            }
        }
        post.setEntity(entity);

        ResponseHandler<String> defaultStringResponseHandler = new ResponseHandler<String>() {

            @Override
            public String handleResponse(HttpResponse httpResponse) throws ClientProtocolException, IOException {
                int status = httpResponse.getStatusLine().getStatusCode();
                if (status >= 200 && status < 300) {
                    HttpEntity entity = httpResponse.getEntity();
                    return entity != null ? EntityUtils.toString(entity) : null;
                } else {
                    throw new ClientProtocolException(String.format("Unexpected response status: %s ; content: %s", status, EntityUtils.toString(entity)));
                }
            }
        };

        String responseText = null;
       */
/* try {
            responseText = client.execute(post, defaultStringResponseHandler);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            post.releaseConnection();
        }*//*

        return responseText;
    }
}
*/
