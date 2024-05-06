package com.example.fakeproduct;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Build;
import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
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

public class viewmycard extends AppCompatActivity {
    EditText e1;
    ListView l1;
    Button b1;
    SharedPreferences sh;
    ArrayList<String> name,image,price,stock,pid;
    String url,pname,url1,oid,amt;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewmycard);

        l1=findViewById(R.id.listproduct);
        b1=findViewById(R.id.button16);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent ik = new Intent(getApplicationContext(),Payment.class);


                ik.putExtra("amt",amt);

                ik.putExtra("oid",oid);
                Toast.makeText(viewmycard.this, "hhh"+amt, Toast.LENGTH_SHORT).show();
                startActivity(ik);



            }
        });

        url1 = "http://" + sh.getString("ip", "") + ":5000/user_view_cart";
        RequestQueue queue = Volley.newRequestQueue(viewmycard.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url1, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {

                    JSONArray ar = new JSONArray(response);
                    Toast.makeText(viewmycard.this, "err"+response, Toast.LENGTH_SHORT).show();

                    name = new ArrayList<>();
                    price = new ArrayList<>();
                    stock = new ArrayList<>();
                    image = new ArrayList<>();
                    pid = new ArrayList<>();


                    for (int i = 0; i < ar.length(); i++) {
                        JSONObject jo = ar.getJSONObject(i);
                        name.add(jo.getString("pname"));
                        price.add(jo.getString("price"));
                        stock.add(jo.getString("quantity"));
                        pid.add(jo.getString("size"));
                        image.add(jo.getString("image"));
                        oid=jo.getString("oid");
                        amt=jo.getString("amt");



                    }

                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);

//                    l1.setAdapter(new CustomViewCart(viewmycard.this, name, image, price, stock, pid));

//                    l1.setOnItemClickListener(viewuser.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(viewmycard.this, "err" + error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("lid", sh.getString("lid",""));
//                        params.put("sid",sid);


                return params;
            }
        };
        queue.add(stringRequest);

    }
    @Override
    public void onBackPressed() {
        Intent ii=new Intent(getApplicationContext(),home.class);
        startActivity(ii);
    }

}

