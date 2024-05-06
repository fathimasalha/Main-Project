package com.example.fakeproduct;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.app.DatePickerDialog;
import android.app.ProgressDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.Toast;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
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
import org.json.JSONException;
import org.json.JSONObject;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;



public class registration extends AppCompatActivity {
    String  name,place,post,pin,phone,email,uname,password;
    EditText e1,e2,e3,e4,e5,e6,e7,e8;
    String res;
    Button b1;
    String fileName = "", path = "";
    private static final int FILE_SELECT_CODE = 0;
    String  obective, house,  father, mother, quardn, relatn;

    String url, ip, lid,title,url1;
    String PathHolder="";
    byte[] filedt=null;
    SharedPreferences sh;
    RadioButton r1,r2;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registration);
        e1=findViewById(R.id.name);
        e2=findViewById(R.id.place);
        e3=findViewById(R.id.post);
        e4=findViewById(R.id.pin);
        e5=findViewById(R.id.phone);
        e6=findViewById(R.id.email);
        e7=findViewById(R.id.username);
        e8=findViewById(R.id.inputPassword);
        b1=findViewById(R.id.button14);



        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        url = "http://" + sh.getString("ip", "") + ":5000/and_registration";
        if (android.os.Build.VERSION.SDK_INT > 9) {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }


        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                name = e1.getText().toString();
                place = e2.getText().toString();
                post = e3.getText().toString();
                pin = e4.getText().toString();

                phone = e5.getText().toString();
                email = e6.getText().toString();
                uname = e7.getText().toString();
                password = e8.getText().toString();

                if(name.equalsIgnoreCase(""))

                {
                    e1.setError("Enter your name");
                }

                else if ( (!name.matches("^[a-zA-Z]+$")))
                {
                    e1.setError("Name should only contain letters");
                }








                else if(place.equalsIgnoreCase(""))
                {
                    e2.setError("Enter place");
                }

                else if ( (!place.matches("^[a-zA-Z]+$")))
                {
                    e2.setError("place should only contain letters");
                }


                else if(post.equalsIgnoreCase(""))
                {
                    e3.setError("Enter post");
                }

                else if ( (!post.matches("^[a-zA-Z]+$")))
                {
                    e3.setError("post should only contain letters");
                }



                else if(pin.equalsIgnoreCase(""))
                {
                    e4.setError("Enter Your Pin");
                }
                else if(pin.length()!=6)
                {
                    e4.setError("invalid pin");
                    e4.requestFocus();
                }




                else if(phone.equalsIgnoreCase(""))
                {
                    e5.setError("Enter Your Phone No");
                }

                else if(!phone.matches("^[9876][0-9]{9}$"))
                {
                    e5.setError("Enter valid phone number");
                    e5.requestFocus();
                }

                else if(email.equalsIgnoreCase(""))
                {
                    e6.setError("Enter Your Email");
                }
                else if(!Patterns.EMAIL_ADDRESS.matcher(email).matches())
                {
                    e6.setError("Enter Valid Email");
                    e6.requestFocus();
                }
                else  if(uname.equalsIgnoreCase(""))
                {
                    e7.setError("Enter username");
                }
                else if(password.equalsIgnoreCase(""))
                {
                    e8.setError("Enter A valid password");
                }
                else if(password.length()<8)
                {
                    e8.setError("invalid  password");
                    e8.requestFocus();
                }







                else {
                    url = "http://" + sh.getString("ip", "") + ":5000/and_registration";

                    RequestQueue queue = Volley.newRequestQueue(registration.this);
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

                                    Toast.makeText(registration.this, "Registration Successful", Toast.LENGTH_SHORT).show();

                                    Intent ik = new Intent(getApplicationContext(), login.class);
                                    startActivity(ik);

                                } else {

                                    Toast.makeText(registration.this, "Invalid username or password", Toast.LENGTH_SHORT).show();

                                }
                            } catch (JSONException e) {
                                Toast.makeText(registration.this, ""+e, Toast.LENGTH_SHORT).show();

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
                params.put("name",name);
                params.put("place",place);
                params.put("post",post);
                params.put("pin",pin);
                params.put("phone",phone);
                params.put("email",email);
                params.put("username",uname);
                params.put("password",password);

                            return params;
                        }
                    };
                    queue.add(stringRequest);


                }
            }
        });
    }
//    ProgressDialog pd;
//    private void uploadBitmap(final String title) {
//        pd=new ProgressDialog(Registration_user.this);
//        pd.setMessage("Uploading....");
//        pd.show();
//        VolleyMultipartRequest volleyMultipartRequest = new VolleyMultipartRequest(Request.Method.POST, url,
//                new Response.Listener<NetworkResponse>() {
//                    @Override
//                    public void onResponse(NetworkResponse response1) {
//                        pd.dismiss();
//                        String x=new String(response1.data);
//                        try {
//                            JSONObject obj = new JSONObject(new String(response1.data));
////                        Toast.makeText(Upload_agreement.this, "Report Sent Successfully", Toast.LENGTH_LONG).show();
//                            if (obj.getString("task").equalsIgnoreCase("valid")) {
//                                Toast.makeText(Registration_user.this, "Successfully uploaded", Toast.LENGTH_LONG).show();
//                                Intent i=new Intent(getApplicationContext(),login.class);
//                                startActivity(i);
//                            } else {
//                                Toast.makeText(getApplicationContext(), obj.getString("task"), Toast.LENGTH_LONG).show();
//                            }
//                        } catch (Exception e) {
//                            Toast.makeText(getApplicationContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
//                        }
//                    }
//                },
//                new Response.ErrorListener() {
//                    @Override
//                    public void onErrorResponse(VolleyError error) {
//                        Toast.makeText(Registration_user.this, error.getMessage(), Toast.LENGTH_SHORT).show();
//                    }
//                }) {
//
//            @Override
//            protected Map<String, String> getParams() throws AuthFailureError {
//                Map<String, String> params = new HashMap<>();
//
//
//
//                params.put("name",name);
//                params.put("place",place);
//                params.put("post",post);
//                params.put("pin",pin);
//                params.put("phone",phone);
//                params.put("email",email);
//                params.put("username",uname);
//                params.put("password",password);
//
////                params.put("lid",sh.getString("lid",""));
//
//                return params;
//            }
//
//            @Override
//            protected Map<String, DataPart> getByteData() {
//                Map<String, DataPart> params = new HashMap<>();
//                params.put("file", new DataPart(PathHolder , filedt ));
//
//
//
//
//
//
//
//
//
//                return params;
//            }
//        };
//
//        Volley.newRequestQueue(this).add(volleyMultipartRequest);
//    }
//
//    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
//    @Override
//    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
//        super.onActivityResult(requestCode, resultCode, data);
//        switch (requestCode) {
//            case 7:
//                if (resultCode == RESULT_OK) {
//                    Uri uri = data.getData();
//                    Log.d("File Uri", "File Uri: " + uri.toString());
//                    // Get the path
//                    try {
//                        PathHolder =FileUtils.getPathFromURI(this, uri);
////                        PathHolder = data.getData().getPath();
////                        Toast.makeText(this, PathHolder, Toast.LENGTH_SHORT).show();
//
//                        filedt = getbyteData(PathHolder,uri);
//                        Log.d("filedataaa", filedt + "");
//                        Toast.makeText(this, filedt.length+"", Toast.LENGTH_SHORT).show();
//                        e7.setText(PathHolder);
//                    }
//                    catch (Exception e){
//                        Toast.makeText(this, ""+e.getMessage(), Toast.LENGTH_SHORT).show();
//                    }
//                }
//                break;
//        }
//    }
//
//
//    private byte[] getbyteData(String pathHolder,Uri suri) {
//        Log.d("path", pathHolder);
//        File fil = new File(pathHolder);
//        int fln = (int) fil.length();
//        byte[] byteArray = null;
//        try {
//            InputStream inputStream = new FileInputStream(fil);
//
//            ByteArrayOutputStream bos = new ByteArrayOutputStream();
//            byte[] b = new byte[fln];
//            int bytesRead = 0;
//
//            while ((bytesRead = inputStream.read(b)) != -1) {
//                bos.write(b, 0, bytesRead);
//            }
//            byteArray = bos.toByteArray();
//            inputStream.close();
//        } catch (Exception e) {
////            Toast.makeText(getApplicationContext(),"++"+e,Toast.LENGTH_LONG).show();
//            File file = new File(pathHolder);
//            if (file.exists()) {
//                Toast.makeText(getApplicationContext(),"file exist",Toast.LENGTH_LONG).show();
//
//            } else {
//
//            }
//            try {
//
//                InputStream inputStream = getContentResolver().openInputStream(suri);
//
////                String ss="com."+pathHolder.split("com.")[1];
////                Uri fileUri = Uri.parse(ss);
////                InputStream inputStream = getContentResolver().openInputStream(fileUri);
//
//
//                ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
//                byte[] buffer = new byte[1024];
//                int bytesRead;
//
//                while ((bytesRead = inputStream.read(buffer)) != -1) {
//                    byteArrayOutputStream.write(buffer, 0, bytesRead);
//                }
//
//                return byteArrayOutputStream.toByteArray();
//            }
//            catch (Exception e1)
//            {
////                tv1.setText(e1+"========================================== =============================== ============================");
////                Toast.makeText(getApplicationContext(),"++="+e1,Toast.LENGTH_LONG).show();
//
//            }
//
//
//
//        }
//        return byteArray;


    }

