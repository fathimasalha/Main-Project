package com.example.fakeproduct;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.GridView;
import android.widget.ImageView;
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

public class Viewproduct extends AppCompatActivity implements AdapterView.OnItemSelectedListener, AdapterView.OnItemClickListener {
    EditText e1;
    Spinner s1;
    Button b1;

    GridView l1;
    SharedPreferences sh;

    ArrayList<String>cat,catid,id,name,price,photo;
    String ciid;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewproduct);
        e1=findViewById(R.id.editTextText2);
        s1=findViewById(R.id.spinner2);
        b1=findViewById(R.id.button2);
        l1=findViewById(R.id.lv1);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());


        String url ="http://"+sh.getString("ip", "") + ":5000/and_category";
        RequestQueue queue = Volley.newRequestQueue(Viewproduct.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);
                    catid= new ArrayList<>();
                    cat= new ArrayList<>();


                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        catid.add(jo.getString("cid"));
                        cat.add(jo.getString("cat"));



                    }

                     ArrayAdapter<String> ad=new ArrayAdapter<>(Viewproduct.this,android.R.layout.simple_list_item_1,cat);
                    s1.setAdapter(ad);
                    s1.setOnItemSelectedListener((AdapterView.OnItemSelectedListener) Viewproduct.this);

//                    l1.setAdapter(new CustomViewProduct(Viewproduct.this,name,id));
//                    l1.setOnItemClickListener(Viewproduct.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {

            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(Viewproduct.this, "err"+error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("shopid", sh.getString("shopid",""));

                return params;
            }
        };
        queue.add(stringRequest);



        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            String pnm=e1.getText().toString();


                String url ="http://"+sh.getString("ip", "") + ":5000/and_vproduct_search";
                RequestQueue queue = Volley.newRequestQueue(Viewproduct.this);

                StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        // Display the response string.
                        Log.d("+++++++++++++++++",response);
                        try {

                            JSONArray ar=new JSONArray(response);
                            id= new ArrayList<>();
                            name= new ArrayList<>();
                            price= new ArrayList<>();
                            photo=new ArrayList<>();

                            for(int i=0;i<ar.length();i++)
                            {
                                JSONObject jo=ar.getJSONObject(i);
                                id.add(jo.getString("id"));
                                name.add(jo.getString("name"));
                                price.add(jo.getString("price"));
                                photo.add(jo.getString("photo"));


                            }

                            // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                            //lv.setAdapter(ad);

                            l1.setAdapter(new CustomViewProduct(Viewproduct.this,name,photo,price,id));
//                    l1.setOnItemClickListener(Viewproduct.this);

                        } catch (Exception e) {
                            Log.d("=========", e.toString());
                        }


                    }

                }, new Response.ErrorListener() {

                    @Override
                    public void onErrorResponse(VolleyError error) {

                        Toast.makeText(Viewproduct.this, "err"+error, Toast.LENGTH_SHORT).show();
                    }
                }) {
                    @Override
                    protected Map<String, String> getParams() {
                        Map<String, String> params = new HashMap<>();
                        params.put("pn", pnm);
                        params.put("cat", ciid);
                        params.put("shopid",sh.getString("shopid",""));

                        return params;
                    }
                };
                queue.add(stringRequest);







            }
        });
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

       String url1 ="http://"+sh.getString("ip", "") + ":5000/and_vproduct";
        RequestQueue queue1 = Volley.newRequestQueue(Viewproduct.this);

        StringRequest stringRequest1 = new StringRequest(Request.Method.POST, url1,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);
                    id= new ArrayList<>();
                    name= new ArrayList<>();
                    price= new ArrayList<>();
                    photo=new ArrayList<>();

                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        id.add(jo.getString("id"));
                        name.add(jo.getString("name"));
                        price.add(jo.getString("price"));
                        photo.add(jo.getString("photo"));


                    }

                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);

                    l1.setAdapter(new CustomViewProduct(Viewproduct.this,name,photo,price,id));
                    l1.setOnItemClickListener(Viewproduct.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {

            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(Viewproduct.this, "err"+error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("shopid",sh.getString("shopid",""));

                return params;
            }
        };
        queue1.add(stringRequest1);




    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        ciid=catid.get(position);
    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Intent ik = new Intent(getApplicationContext(), ViewShop.class);
        startActivity(ik);

    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long ids) {

        SharedPreferences.Editor ed=sh.edit();
        ed.putString("pid",id.get(position));
        ed.commit();
        Intent ik = new Intent(getApplicationContext(), ViewProductDetails.class);
        startActivity(ik);


    }
}