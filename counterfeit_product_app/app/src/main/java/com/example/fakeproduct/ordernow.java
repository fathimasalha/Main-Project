package com.example.fakeproduct;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class ordernow extends AppCompatActivity {
    ImageButton btadd,btmin;
    Button b1;
    Spinner s1;
    TextView t1;
    SharedPreferences sh;

    int count=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ordernow);
//        btadd=findViewById(R.id.imageButton21);
//        btmin=findViewById(R.id.imageButton1);
//        s1=findViewById(R.id.spinner1);
//        t1=findViewById(R.id.textView21);
//        b1=findViewById(R.id.button41);
//        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
//
//        String size=sh.getString("size","");
//        String [] ls=size.split("");
//        ArrayAdapter<String> ad=new ArrayAdapter<>(ordernow.this,android.R.layout.simple_list_item_1,ls);
//        s1.setAdapter(ad);
//
//        String amtString = sh.getString("pre", ""); // Get the amount string from SharedPreferences
//        double amount = Double.parseDouble(amtString); // Parse the amount string to double
//        int quantity = Integer.parseInt(t1.getText().toString()); // Parse the quantity from the text view
//        double totalAmount = amount * quantity;
//        btadd.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                count=count+1;
//                t1.setText(String.valueOf(count));
//
//                Toast.makeText(ordernow.this, "-----count-"+count, Toast.LENGTH_SHORT).show();
//
//            }
//        });
//        btmin.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                if (count>0) {
//                    count = count -1;
//                    t1.setText(String.valueOf(count));
//
//                    Toast.makeText(ordernow.this, "-----count-"+count, Toast.LENGTH_SHORT).show();
//
//                }
//
//            }
//        });
//        b1.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                if(t1.getText().toString().equalsIgnoreCase("0")){
//                    t1.setError("Add Quantity");
//                }else {
//                    String url = "http://" + sh.getString("ip", "") + ":5000/ordrprdctcodeand";
//                    RequestQueue queue = Volley.newRequestQueue(ordernow.this);
//
//                    StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
//                        @Override
//                        public void onResponse(String response) {
//                            // Display the response string.
//                            Toast.makeText(ordernow.this, "jj"+response, Toast.LENGTH_SHORT).show();
//                            Log.d("+++++++++++++++++", response);
//                            try {
//
//                                JSONObject json = new JSONObject(response);
//                                String res = json.getString("task");
//                                String amt = json.getString("amt");
//                                String oid = json.getString("oid");
//                                Toast.makeText(ordernow.this, "Successful"+amt+"==="+oid, Toast.LENGTH_SHORT).show();
//
//                                if (res.equalsIgnoreCase("valid")) {
//
//                                    Toast.makeText(ordernow.this, "Successful", Toast.LENGTH_SHORT).show();
//
//                                    Intent ik = new Intent(getApplicationContext(), Payment.class);
//                                    ik.putExtra("amt",amt);
//                                    ik.putExtra("oid",oid);
//                                    startActivity(ik);
//
//                                } else {
//
//                                    Toast.makeText(ordernow.this, "Invalid username or password", Toast.LENGTH_SHORT).show();
//
//                                }
//                            } catch (Exception e) {
//                                Log.d("=========", e.toString());
//                            }
//
//
//                        }
//
//                    }, new Response.ErrorListener() {
//                        @Override
//                        public void onErrorResponse(VolleyError error) {
//
//                            Toast.makeText(ordernow.this, "err" + error, Toast.LENGTH_SHORT).show();
//                        }
//                    }) {
//                        @Override
//                        protected Map<String, String> getParams() {
//                            Map<String, String> params = new HashMap<>();
//                            params.put("srid", sh.getString("pid", ""));
//                            params.put("quantity", t1.getText().toString());
//                            params.put("lid", sh.getString("lid", ""));
//                            params.put("size", s1.getSelectedItem().toString());
//
//                            return params;
//                        }
//                    };
//                    queue.add(stringRequest);
//                }
//
//            }
//        });


    }
}