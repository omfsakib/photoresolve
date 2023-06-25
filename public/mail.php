<?php 

    $reffer =  $_SERVER['HTTP_REFERER'];
    
    if($reffer != 'https://photoresolve.com')
    {
        header('Location: /contact');
    }
    
    /* 
     *  Prevent Request
     *  Prevent to next step if request type is not POST
     */ 
     
    if ($_SERVER['REQUEST_METHOD'] != 'POST')
    {
        header('Location: /contact');   
    }


    /* 
     *  Validation Request Data 
     */ 

    if(isset($_POST))
    {
        $get_Name       = filter_var($_POST['name'], FILTER_SANITIZE_STRING);
        $get_Email      = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
        $get_Message    = filter_var($_POST['message'], FILTER_SANITIZE_STRING);
         
        
        if(
            !empty($get_Name ) && 
            !empty($get_Email) && 
            !empty($get_Message)
        ){ 
            sentMail($get_Email, $get_Name, $get_Message); 
        }
         
    }
    
    
    function sentMail($email, $name, $get_Message)
    {
        $email = filter_var($email, FILTER_VALIDATE_EMAIL);
        
 
        //send email 
        if( !empty($email) )
        { 
            
            /* 
             *  Mail Setting 
             */  
            $receiveEmail   = 'hellophotoresolve@gmail.com';
            $subject        = 'contact form'; 
            
            // To send HTML mail, the Content-type header must be set
            $headers    = 'MIME-Version: 1.0' . "\r\n";
            $headers   .= 'Content-type: text/html; charset=UTF-8' . "\r\n"; 
            $headers   .= 'From: info@photoresolve.com' . "\r\n";
            $headers   .= 'Reply-To: '.$email. "\r\n";
    
            
           // Compose a simple HTML email message
                $message   = '<html><body>';
                $message  .= sprintf('<b> Name: </b> %s <br/>', $name);
                $message  .= sprintf('<b> Email: </b> %s <br/>', $email);
                $message  .= sprintf('<b> Message: </b> %s <br/>', $get_Message);
                $message  .= '</body></html>';
                
    
            $sent = mail($receiveEmail, $subject, $message, $headers);
            
            if($sent)
            {
                header('Location: /contact');
            } 
            
        }
        
    }