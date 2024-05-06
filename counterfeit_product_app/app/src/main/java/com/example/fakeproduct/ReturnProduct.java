package com.example.fakeproduct;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class ReturnProduct extends AppCompatActivity {
    TextView t1, tv2, tv3,tv4,tv5,tv6,tv7;
    ImageView im;
    EditText e1;
    Button b1;
    String Reason,url,url1;
    ArrayList<String> id,name,price,quantity,photo,size,date,status;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_return_product);
        t1=findViewById(R.id.textView6);
        tv2=findViewById(R.id.tvroom);
        tv3=findViewById(R.id.tvhallk);
        tv4=findViewById(R.id.tvhall7);
        tv5=findViewById(R.id.tvhall);
        tv6=findViewById(R.id.tvh);
        tv7=findViewById(R.id.tv);
        im=findViewById(R.id.imgaprtmnt);

        e1=findViewById(R.id.editTextText4);
        b1=findViewById(R.id.button8);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());


        RequestQueue queue = Volley.newRequestQueue(ReturnProduct.this);
        url1 = "http://" + sh.getString("ip", "") + ":5000/and_vreturn_info";
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url1,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);

                    {
                        JSONObject jo=ar.getJSONObject(0);
                        tv2.setText(jo.getString("pname"));
                        tv3.setText(jo.getString("price"));
                        tv4.setText(jo.getString("quantity"));
                        tv5.setText(jo.getString("size"));
                        tv6.setText(jo.getString("date"));
                        tv7.setText(jo.getString("status"));


                        if(android.os.Build.VERSION.SDK_INT>9)
                        {
                            StrictMode.ThreadPolicy policy=new StrictMode.ThreadPolicy.Builder().permitAll().build();
                            StrictMode.setThreadPolicy(policy);
                        }

//        i2.setImageDrawable(Drawable.createFromPath(getIntent().getStringExtra("photo"))));
                        java.net.URL thumb_u;
                        try {

                            //thumb_u = new java.net.URL("http://192.168.43.57:5000/static/photo/flyer.jpg");

                            thumb_u = new java.net.URL("http://"+sh.getString("ip","")+":5000/"+jo.getString("photo"));
                            Drawable thumb_d = Drawable.createFromStream(thumb_u.openStream(), "src");
                            im.setImageDrawable(thumb_d);

                        }
                        catch (Exception e)
                        {
                            Log.d("errsssssssssssss",""+e);
                        }
                    }


                } catch (JSONException e) {
                    e.printStackTrace();
                }

            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(getApplicationContext(),"Error",Toast.LENGTH_LONG).show();
            }
        }){
            @Override
            protected Map<String, String> getParams()
            {
                Map<String, String>  params = new HashMap<String, String>();
                params.put("o_id", getIntent().getStringExtra("od_id"));

                params.put("uid", sh.getString("lid", ""));


                return params;
            }
        };
        // Add the request to the RequestQueue.
        queue.add(stringRequest);




        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Reason = e1.getText().toString();

                if (Reason.equalsIgnoreCase("")) {
                    e1.setError("Enter your reason");
                } else {
                    url = "http://" + sh.getString("ip", "") + ":5000/and_return_product";

                    RequestQueue queue = Volley.newRequestQueue(ReturnProduct.this);
//                    url = "http://" + sh.getString("ip","") + ":5000/and_logincode";

                    // Request a string response from the provided URL.
                    StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            // Display the response string.
                            Log.d("+++++++++++++++++", response);
                            try {
                                JSONObject json = new JSONObject(response);
                                String res = json.getString("task");

                                if (res.equalsIgnoreCase("valid")) {

                                    Toast.makeText(ReturnProduct.this, "Return Details Submitted", Toast.LENGTH_SHORT).show();

                                    Intent ik = new Intent(getApplicationContext(), home.class);
                                    startActivity(ik);

                                } else {

//                                    Toast.makeText(ReturnProduct.this, "Invalid username or password", Toast.LENGTH_SHORT).show();

                                }
                            } catch (JSONException e) {
                                Toast.makeText(ReturnProduct.this, "" + e, Toast.LENGTH_SHORT).show();

                                e.printStackTrace();
                            }


                        }
                    }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {


                            Toast.makeText(getApplicationContext(), "Error" + error, Toast.LENGTH_LONG).show();
                        }
                    }) {
                        @Override
                        protected Map<String, String> getParams() {
                            Map<String, String> params = new HashMap<String, String>();
                            params.put("Reason", Reason);
                            params.put("oid", getIntent().getStringExtra("od_id"));


                            return params;
                        }
                    };
                    queue.add(stringRequest);


                }
            }
        });


    }
}