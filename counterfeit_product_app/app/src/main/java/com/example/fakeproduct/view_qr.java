package com.example.fakeproduct;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.drawable.Drawable;
import android.preference.PreferenceManager;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class view_qr extends AppCompatActivity {
    TextView t1,t2,t4,t5,t6,t7,t8,t9,t10,t12,tv4,tv5,tv6;
    Button b,b2;
    ImageView img;
    String srno,url,urll;
    SharedPreferences sh;
    @Override
    public void onBackPressed() {
        Intent ins=new Intent(getApplicationContext(),home.class);
        startActivity(ins);
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_qr);
        t1=(TextView) findViewById(R.id.textView8);
        t2=(TextView) findViewById(R.id.textView10);
        t4=(TextView) findViewById(R.id.textView14);
        t5=(TextView) findViewById(R.id.textView16);
        t6=(TextView) findViewById(R.id.textView7);
        t7=(TextView) findViewById(R.id.textView9);
        t9=(TextView) findViewById(R.id.textView13);
        t10=(TextView) findViewById(R.id.textView15);

        t12=(TextView) findViewById(R.id.textView17);
        tv4=(TextView) findViewById(R.id.textView4);
        tv5=(TextView) findViewById(R.id.textView5);
        tv6=(TextView) findViewById(R.id.textView6);
        img= findViewById(R.id.imageView3);





        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        srno = ScanQR.contents;//getting id from scan qr
        String hu = sh.getString("url", "");
//        url = hu + "andviewproducts";

        url="http://"+sh.getString("ip", "") + ":5000/andviewproducts";
        Toast.makeText(getApplicationContext(), url , Toast.LENGTH_SHORT).show();

        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
        StringRequest postRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {

            @Override
            public void onResponse(String response) {
                // Display the response string.

                Toast.makeText(getApplicationContext(), "QR Code Verified" , Toast.LENGTH_SHORT).show();
                try {
                    JSONObject jsonObj1 = new JSONObject(response);

                    Toast.makeText(view_qr.this, "===="+response, Toast.LENGTH_SHORT).show();
                    if (jsonObj1.getString("task").equalsIgnoreCase("product")) {

//                        JSONObject jsonObj=jsonObj1.getJSONObject("result");
                        tv4.setText(jsonObj1.getString("manu"));
                        tv5.setText(jsonObj1.getString("dis"));
                        tv6.setText(jsonObj1.getString("pha"));
                        t12.setVisibility(View.GONE);


                        java.net.URL thumb_u;
                        try {

                            //thumb_u = new java.net.URL("http://192.168.43.57:5000/static/photo/flyer.jpg");

                            thumb_u = new java.net.URL("http://"+sh.getString("ip","")+":5000"+jsonObj1.getString("img"));
                            Drawable thumb_d = Drawable.createFromStream(thumb_u.openStream(), "src");
                            img.setImageDrawable(thumb_d);

                        }
                        catch (Exception e)
                        {
                            Toast.makeText(view_qr.this, ""+e, Toast.LENGTH_SHORT).show();
                            Log.d("errsssssssssssss",""+e);
                        }
                        t1.setText(jsonObj1.getString("med"));
                        t2.setText(jsonObj1.getString("mf"));
                        t4.setText(jsonObj1.getString("size"));
                        t5.setText(jsonObj1.getString("price"));
//                        t.setText(jsonObj1.getString("info"));
                    } else {
                        t9.setVisibility(View.INVISIBLE);
                        t10.setVisibility(View.INVISIBLE);
                        tv4.setVisibility(View.INVISIBLE);
                        tv5.setVisibility(View.INVISIBLE);
                        tv6.setVisibility(View.INVISIBLE);
                        t12.setVisibility(View.VISIBLE);
                        t1.setVisibility(View.INVISIBLE);
                        t2.setVisibility(View.INVISIBLE);
                        t4.setVisibility(View.INVISIBLE);
                        t5.setVisibility(View.INVISIBLE);
                        t6.setVisibility(View.INVISIBLE);
                        t7.setVisibility(View.INVISIBLE);
                        t8.setVisibility(View.INVISIBLE);


//                        b2.setVisibility(View.VISIBLE);

                    }
                } catch (Exception e) {
                    Toast.makeText(getApplicationContext(), "eeeee" + e.toString(), Toast.LENGTH_SHORT).show();

                    Log.d("=========", e.toString());
                    Toast.makeText(view_qr.this, ""+e, Toast.LENGTH_SHORT).show();
                }
            }
        },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // error
                        Toast.makeText(getApplicationContext(), "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
                    }
                }
        ) {

            //                value Passing android to python
            @Override
            protected Map<String, String> getParams() {
                SharedPreferences sp = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                Map<String, String> params = new HashMap<String, String>();
                params.put("srno", srno);//passing to python
                return params;
            }
        };

        int MY_SOCKET_TIMEOUT_MS=120000;

        postRequest.setRetryPolicy(new DefaultRetryPolicy(
                MY_SOCKET_TIMEOUT_MS,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
        requestQueue.add(postRequest);
    }


}