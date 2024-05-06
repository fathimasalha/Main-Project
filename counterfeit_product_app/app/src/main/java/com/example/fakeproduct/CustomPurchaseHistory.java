package com.example.fakeproduct;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.GridView;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class CustomPurchaseHistory extends BaseAdapter {
    private Context context;
    ArrayList<String> a;
    ArrayList<String> b;
    ArrayList<String> c;
    ArrayList<String> d;
    ArrayList<String> e;
    ArrayList<String> f;
    ArrayList<String> g;
    ArrayList<String> h;
    ArrayList<String> i;
    ArrayList<String> j;
    ArrayList<String>name,price,photo,size,quantity,total,date,status,id;
    SharedPreferences sh;




    public CustomPurchaseHistory(Context applicationContext, ArrayList<String> a, ArrayList<String> b, ArrayList<String> c, ArrayList<String> d,ArrayList<String> e,ArrayList<String> g,ArrayList<String> h,ArrayList<String> i,ArrayList<String> j) {
        // TODO Auto-generated constructor stub
        this.context=applicationContext;
        this.a=a;
        this.b=b;
        this.c=c;
        this.d=d;
        this.e=e;
        this.f=f;
        this.g=g;
        this.h=h;
        this.i=i;
        this.j=j;
        sh= PreferenceManager.getDefaultSharedPreferences(applicationContext);
    }

    @Override
    public int getCount() {
        // TODO Auto-generated method stub
        return a.size();
    }

    @Override
    public Object getItem(int arg0) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public long getItemId(int arg0) {
        // TODO Auto-generated method stub
        return 0;
    }
    @Override
    public int getItemViewType(int arg0) {
        // TODO Auto-generated method stub
        return 0;
    }


    @Override
    public View getView(int position, View convertview, ViewGroup parent) {
        // TODO Auto-generated method stub
        LayoutInflater inflator=(LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View ListView;
        if(convertview==null)
        {
            ListView=new View(context);
            ListView=inflator.inflate(R.layout.activity_custom_purchase_history, null);

        }
        else
        {
            ListView=(View)convertview;

        }
        TextView tv1=(TextView)ListView.findViewById(R.id.tvroom);
        ImageView i1=(ImageView) ListView.findViewById(R.id.imgaprtmnt);
        TextView tv2=(TextView)ListView.findViewById(R.id.tvhall);
        TextView tv3=(TextView)ListView.findViewById(R.id.tvhall7);
        TextView tv4=(TextView)ListView.findViewById(R.id.tvhallk);
        TextView tv5=(TextView)ListView.findViewById(R.id.tvh);
        TextView tv6=(TextView)ListView.findViewById(R.id.tv);
        Button b1= (Button) ListView.findViewById(R.id.button5);
        if(j.get(position).equalsIgnoreCase("yes")){
            b1.setEnabled(false);
            b1.setText("Returned");
        }
        else{
            b1.setEnabled(true);
            b1.setText("Return");
        }
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {


                Intent ik = new Intent(context.getApplicationContext(), ReturnProduct.class);
                ik.putExtra("od_id", i.get(position));
                context.startActivity(ik);

            }
        });


        if (android.os.Build.VERSION.SDK_INT > 9) {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }
        java.net.URL thumb_u;
        try {

            //thumb_u = new java.net.URL("http://192.168.43.57:5000/static/photo/flyer.jpg");

            thumb_u = new java.net.URL("http://"+sh.getString("ip","")+":5000"+c.get(position));
            Drawable thumb_d = Drawable.createFromStream(thumb_u.openStream(), "src");
            i1.setImageDrawable(thumb_d);

        }
        catch (Exception e)
        {
            Log.d("errsssssssssssss",""+e);
        }


        tv1.setText(a.get(position));
        tv2.setText(b.get(position));
        tv3.setText(d.get(position));
        tv4.setText(e.get(position));
        tv5.setText(h.get(position));
        tv6.setText(g.get(position));





        tv1.setTextColor(Color.BLACK);
        tv2.setTextColor(Color.BLACK);
        tv3.setTextColor(Color.BLACK);
        tv4.setTextColor(Color.BLACK);
        tv5.setTextColor(Color.BLACK);
        tv6.setTextColor(Color.BLACK);











        return ListView;

    }

}

