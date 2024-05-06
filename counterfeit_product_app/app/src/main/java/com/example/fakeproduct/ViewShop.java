package com.example.fakeproduct;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Spinner;
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

public class ViewShop extends AppCompatActivity {
    EditText e1;

    Button b1;
    ListView l1;
    SharedPreferences sh;
    ArrayList id,name,place,phone,email,photo;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_shop);
        e1=findViewById(R.id.editTextText2);
        b1=findViewById(R.id.button2);
        l1=findViewById(R.id.lv1);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {


                String snm=e1.getText().toString();
                sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

                String url ="http://"+sh.getString("ip", "") + ":5000/and_vshop_search";
                RequestQueue queue = Volley.newRequestQueue(ViewShop.this);

                StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // Display the response string.
                        Log.d("+++++++++++++++++",response);
                        try {

                            JSONArray ar=new JSONArray(response);
                            id= new ArrayList<>();
                            name= new ArrayList<>();
                            place= new ArrayList<>();
                            phone= new ArrayList<>();
                            email= new ArrayList<>();
                            photo=new ArrayList<>();

                            for(int i=0;i<ar.length();i++)
                            {
                                JSONObject jo=ar.getJSONObject(i);
                                id.add(jo.getString("id"));
                                name.add(jo.getString("name"));
                                place.add(jo.getString("place"));
                                phone.add(jo.getString("phone"));
                                email.add(jo.getString("email"));
                                photo.add(jo.getString("photo"));


                            }

                            // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                            //lv.setAdapter(ad);

                            l1.setAdapter(new CustomViewShop(ViewShop.this,name,photo,place,phone,email,id));
//                    l1.setOnItemClickListener(Viewproduct.this);

                        } catch (Exception e) {
                            Log.d("=========", e.toString());
                        }


                    }

                }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {

                        Toast.makeText(ViewShop.this, "err"+error, Toast.LENGTH_SHORT).show();
                    }
                }) {
                    @Override
                    protected Map<String, String> getParams() {
                        Map<String, String> params = new HashMap<>();
                        params.put("sn", snm);
                        return params;
                    }
                };
                queue.add(stringRequest);


            }
        });
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        String url ="http://"+sh.getString("ip", "") + ":5000/and_vshop";
        RequestQueue queue = Volley.newRequestQueue(ViewShop.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);
                    id= new ArrayList<>();
                    name= new ArrayList<>();
                    place= new ArrayList<>();
                    phone= new ArrayList<>();
                    email= new ArrayList<>();
                    photo=new ArrayList<>();

                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        id.add(jo.getString("id"));
                        name.add(jo.getString("name"));
                        place.add(jo.getString("place"));
                        phone.add(jo.getString("phone"));
                        email.add(jo.getString("email"));
                        photo.add(jo.getString("photo"));


                    }

                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);

                    l1.setAdapter(new CustomViewShop(ViewShop.this,name,photo,place,phone,email,id));
//                    l1.setOnItemClickListener(Viewproduct.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(ViewShop.this, "err"+error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();

                return params;
            }
        };
        queue.add(stringRequest);






    }
}