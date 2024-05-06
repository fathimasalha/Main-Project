package com.example.fakeproduct;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
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

public class PurchaseHistory extends AppCompatActivity {
    ListView l1;
    SharedPreferences sh;
    String url1,oid,amt;
    ArrayList<String> id,name,price,quantity,photo,size,date,status,sss;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_purchase_history);
        l1=findViewById(R.id.lv1);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());


        url1 ="http://"+sh.getString("ip", "") + ":5000/and_vpurchase_history";
        RequestQueue queue1 = Volley.newRequestQueue(PurchaseHistory.this);
        StringRequest stringRequest1 = new StringRequest(Request.Method.POST, url1,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
//                Toast.makeText(PurchaseHistory.this, "======"+response, Toast.LENGTH_SHORT).show();

                try {
                    JSONArray ar = new JSONArray(response);
//                    String res = json.getString("amt");
//                    Toast.makeText(ViewCart.this, "======"+response, Toast.LENGTH_SHORT).show();

//                    JSONObject ar1 = new JSONObject(json.getString("data"));
//                    String tp = ar1.getString("total");
//                    SharedPreferences.Editor edp = sh.edit();
//                    edp.putString("tott", res);
//                    edp.commit();
//                    t2.setText(res);
//                    JSONArray ar = new JSONArray(json.getString("data"));
//                    Toast.makeText(PurchaseHistory.this, "ppppppp"+response, Toast.LENGTH_SHORT).show();
                    id= new ArrayList<>();
                    name= new ArrayList<>();
                    price= new ArrayList<>();
                    photo=new ArrayList<>();
                    quantity=new ArrayList<>();
                    size=new ArrayList<>();
//                    total=new ArrayList<>();
                    date=new ArrayList<>();
                    status=new ArrayList<>();
                    sss=new ArrayList<>();
//                    amonut=new ArrayList<>();
                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        id.add(jo.getString("id"));
                        name.add(jo.getString("pname"));
                        price.add(jo.getString("price"));
                        photo.add(jo.getString("photo"));
                        quantity.add(jo.getString("quantity"));
                        size.add(jo.getString("size"));
//                        total.add(jo.getString("total"));
                        date.add(jo.getString("date"));
                        status.add(jo.getString("status"));
                        sss.add(jo.getString("res"));
//                        oid = jo.getString("oid");
//                        amt = jo.getString("amt");
//                        t2.setText(jo.getString("amt"));
                    }
                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);

                    l1.setAdapter(new CustomPurchaseHistory(PurchaseHistory.this,name,price,photo,quantity,size,status,date,id,sss));

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {

            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(PurchaseHistory.this, "err"+error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("lid",sh.getString("lid",""));

                return params;
            }
        };
        queue1.add(stringRequest1);


    }
}