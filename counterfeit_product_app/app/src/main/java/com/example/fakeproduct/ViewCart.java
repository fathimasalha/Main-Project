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
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
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

public class ViewCart extends AppCompatActivity {



    ListView l1;
    String tamt="";
    SharedPreferences sh;
    TextView t1,t2;
    Button b1;
    String url,pname,url1,oid,amt,gst;

    ArrayList<String>name,price,photo,size,quantity,id,amonut;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_cart);
        l1=findViewById(R.id.lv1);
        t1=findViewById(R.id.textView5);
        t2=findViewById(R.id.textView4);
        b1=findViewById(R.id.button15);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());



//        b1.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                Intent ik = new Intent(getApplicationContext(),ViewCart.class);
//
////                                ik.putExtra("oid",id.get(position));
////                                ik.putExtra("p",d.get(position));
////                                context.startActivity(ik);
////                                Toast.makeText(context, "place order", Toast.LENGTH_SHORT).show();
//
//
//                ik.putExtra("p",sh.getString("tott",""));
//
//                ik.putExtra("oid",oid);
//                Toast.makeText(ViewCart.this, "hhh"+amt, Toast.LENGTH_SHORT).show();
//                startActivity(ik);
//
//
//
//            }
//        });




        url1 ="http://"+sh.getString("ip", "") + ":5000/user_view_cart";
        RequestQueue queue1 = Volley.newRequestQueue(ViewCart.this);
        StringRequest stringRequest1 = new StringRequest(Request.Method.POST, url1,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {
                    JSONObject json = new JSONObject(response);
//                    String res = json.getString("amt");
//                    Toast.makeText(ViewCart.this, "======"+response, Toast.LENGTH_SHORT).show();

//                    JSONObject ar1 = new JSONObject(json.getString("data"));
//                    String tp = ar1.getString("total");
//                    SharedPreferences.Editor edp = sh.edit();
//                    edp.putString("tott", res);
//                    edp.commit();
//                    t2.setText(res);
                    JSONArray ar = new JSONArray(json.getString("data"));
//                    Toast.makeText(ViewCart.this, "ppppppp"+response, Toast.LENGTH_SHORT).show();
                    id= new ArrayList<>();
                    name= new ArrayList<>();
                    price= new ArrayList<>();
                    photo=new ArrayList<>();
                    quantity=new ArrayList<>();
                    size=new ArrayList<>();
//                    amonut=new ArrayList<>();
                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        id.add(jo.getString("odid"));
                        name.add(jo.getString("pname"));
                        price.add(jo.getString("price"));
                        photo.add(jo.getString("image"));
                        quantity.add(jo.getString("quantity"));
                        size.add(jo.getString("size"));
//                        amonut.add(jo.getString("amt"));
                        oid = jo.getString("oid");
                        amt = jo.getString("amt");
                        gst = jo.getString("gst");
                        Float aaa=Float.parseFloat(amt)+(Float.parseFloat(amt)*.08f);
                        String amtttt= "Sub Total : "+amt+"\n";
                               amtttt+="GST 8%    : "+ (Float.parseFloat(amt)*.08f)+"\n";
                               amtttt+="Total          : "+ gst;
                        t2.setText(amtttt);
                        tamt=aaa.toString().substring(0,aaa.toString().toString().length()-3);
//                        t2.setText(jo.getString("amt"));
                    }
                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);

                    l1.setAdapter(new CustomViewCart(ViewCart.this,name,photo,price,quantity,size,id));

                } catch (Exception e) {
                    Toast.makeText(getApplicationContext(),e+"",Toast.LENGTH_SHORT).show();
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {

            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(ViewCart.this, "err"+error, Toast.LENGTH_SHORT).show();
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
        stringRequest1.setRetryPolicy(new DefaultRetryPolicy(
                10000,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
        queue1.add(stringRequest1);


        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent ik = new Intent(getApplicationContext(),Payment.class);


                ik.putExtra("amt",gst);

                ik.putExtra("oid",oid);
                Toast.makeText(ViewCart.this, "hhh"+gst, Toast.LENGTH_SHORT).show();
                startActivity(ik);

            }
        });

    }


    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Intent ik = new Intent(getApplicationContext(), home.class);
        startActivity(ik);



    }
}