package com.example.fakeproduct;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;
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

public class ViewProductDetails extends AppCompatActivity {
    TextView t1, t2, t3, t4, t5;
    Button  b2;
    ImageView i;
    ImageButton btadd, btmin;
    Button b1;
    Spinner s1;
    TextView t11;
    SharedPreferences sh;
    String gst;
    int count=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_product_details);
        t1 = findViewById(R.id.tvr);
        t2 = findViewById(R.id.tvh);
        t3 = findViewById(R.id.tvk);
        t4 = findViewById(R.id.tvl);
        t5 = findViewById(R.id.tvm);
        i = findViewById(R.id.img);
        btadd = findViewById(R.id.imageButton21);
        btmin = findViewById(R.id.imageButton1);
        s1 = findViewById(R.id.spinner1);
        t11 = findViewById(R.id.textView21);
        b2 = findViewById(R.id.button7);
        b1 = findViewById(R.id.button5);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
//
        String url = "http://" + sh.getString("ip", "") + ":5000/and_vone_productdet";
        RequestQueue queue = Volley.newRequestQueue(ViewProductDetails.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {
                    JSONObject json = new JSONObject(response);
                    String res = json.getString("task");


                    if (res.equalsIgnoreCase("valid")) {
                        String name = json.getString("name");
                        String price = json.getString("price");
                        String photo = json.getString("image");
                        String desc = json.getString("desc");
                        String cate = json.getString("cat");
                        String size = json.getString("size");

                        t1.setText(name);
                        t2.setText(price);
                        t3.setText(desc);
                        t4.setText(cate);
                        t5.setText(size);
                        SharedPreferences.Editor ed = sh.edit();
                        ed.putString("size", size);
                        ed.putString("pre", price);
                        ed.commit();

                        String[] ls = size.split("");
                        ArrayAdapter<String> ad = new ArrayAdapter<>(ViewProductDetails.this, android.R.layout.simple_list_item_1, ls);
                        s1.setAdapter(ad);
                        java.net.URL thumb_u;
                        try {

                            //thumb_u = new java.net.URL("http://192.168.43.57:5000/static/photo/flyer.jpg");

                            thumb_u = new java.net.URL("http://" + sh.getString("ip", "") + ":5000" + photo);
                            Drawable thumb_d = Drawable.createFromStream(thumb_u.openStream(), "src");
                            i.setImageDrawable(thumb_d);

                        } catch (Exception e) {
                            Log.d("errsssssssssssss", "" + e);
                        }


                    } else {

                        Toast.makeText(ViewProductDetails.this, "Invalid username or password", Toast.LENGTH_SHORT).show();

                    }


//                    l1.setAdapter(new CustomViewProduct(Viewproduct.this,name,id));
//                    l1.setOnItemClickListener(Viewproduct.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {

            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(ViewProductDetails.this, "err" + error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("pid", sh.getString("pid", ""));
                params.put("shopid", sh.getString("shopid", ""));

                return params;
            }
        };
        queue.add(stringRequest);
//
////
//
//        b1.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//
//                Intent ik = new Intent(getApplicationContext(), AddToCart.class);
//
//                startActivity(ik);
//
//            }
//        });
//
//
//

//
    String amtString = sh.getString("pre", ""); // Get the amount string from SharedPreferences
    double amount = Double.parseDouble(amtString); // Parse the amount string to double
    int quantity = Integer.parseInt(t11.getText().toString()); // Parse the quantity from the text view
    double totalAmount = amount * quantity;
        btadd.setOnClickListener(new View.OnClickListener()

    {
        @Override
        public void onClick (View v){
        count = count + 1;
        t11.setText(String.valueOf(count));

        Toast.makeText(ViewProductDetails.this, "-----count-" + count, Toast.LENGTH_SHORT).show();

    }
    });
        btmin.setOnClickListener(new View.OnClickListener()

    {
        @Override
        public void onClick (View v){
        if (count > 0) {
            count = count - 1;
            t11.setText(String.valueOf(count));

            Toast.makeText(ViewProductDetails.this, "-----count-" + count, Toast.LENGTH_SHORT).show();

        }

    }
    });
        b2.setOnClickListener(new View.OnClickListener()

    {
        @Override
        public void onClick (View v){
        if (t11.getText().toString().equalsIgnoreCase("0")) {
            t11.setError("Add Quantity");
        } else {
            String url = "http://" + sh.getString("ip", "") + ":5000/ordrprdctcodeand";
            RequestQueue queue = Volley.newRequestQueue(ViewProductDetails.this);

            StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    // Display the response string.
                    Toast.makeText(ViewProductDetails.this, "jj" + response, Toast.LENGTH_SHORT).show();
                    Log.d("+++++++++++++++++", response);
                    try {

                        JSONObject json = new JSONObject(response);
                        String res = json.getString("task");
                        String amt = json.getString("gst");
                        String oid = json.getString("oid");
                        Toast.makeText(ViewProductDetails.this, "Successful==="+ amt + "===" + oid, Toast.LENGTH_SHORT).show();

                        if (res.equalsIgnoreCase("valid")) {

                            Toast.makeText(ViewProductDetails.this, "Successful", Toast.LENGTH_SHORT).show();

                            Intent ik = new Intent(getApplicationContext(), Payment.class);
                            ik.putExtra("amt", amt);
                            ik.putExtra("oid", oid);
                            startActivity(ik);

                        } else {

                            Toast.makeText(ViewProductDetails.this, "Failed", Toast.LENGTH_SHORT).show();

                        }
                    } catch (Exception e) {
                        Log.d("=========", e.toString());
                    }


                }

            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {

                    Toast.makeText(ViewProductDetails.this, "err" + error, Toast.LENGTH_SHORT).show();
                }
            }) {
                @Override
                protected Map<String, String> getParams() {
                    Map<String, String> params = new HashMap<>();
                    params.put("srid", sh.getString("pid", ""));
                    params.put("quantity", t11.getText().toString());
                    params.put("lid", sh.getString("lid", ""));
                    params.put("size", s1.getSelectedItem().toString());

                    return params;
                }
            };
            queue.add(stringRequest);
        }

    }
    });
b1.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {

        if(t1.getText().toString().equalsIgnoreCase("0")){
            t1.setError("Add Quantity");
        }else {
            String url = "http://" + sh.getString("ip", "") + ":5000/add_to_cart";
            RequestQueue queue = Volley.newRequestQueue(ViewProductDetails.this);
            StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    // Display the response string.
                    Log.d("+++++++++++++++++", response);
                    try {

                        JSONObject json = new JSONObject(response);
                        String res = json.getString("task");

                        if (res.equalsIgnoreCase("valid")) {

                            Toast.makeText(ViewProductDetails.this, "Successful", Toast.LENGTH_SHORT).show();

                            Intent ik = new Intent(getApplicationContext(),Viewproduct.class);
                            startActivity(ik);

                        } else {

                            Toast.makeText(ViewProductDetails.this, "OUT OF STOCK", Toast.LENGTH_SHORT).show();

                        }
                    } catch (Exception e) {
                        Log.d("=========", e.toString());
                    }


                }

            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {

                    Toast.makeText(ViewProductDetails.this, "err" + error, Toast.LENGTH_SHORT).show();
                }
            }) {
                @Override
                protected Map<String, String> getParams() {
                    Map<String, String> params = new HashMap<>();
                    params.put("srid", sh.getString("pid", ""));
                    params.put("quantity", t11.getText().toString());
                    params.put("lid", sh.getString("lid", ""));
                    params.put("size", s1.getSelectedItem().toString());

                    return params;
                }
            };
            queue.add(stringRequest);

        }
        }
});
}
}