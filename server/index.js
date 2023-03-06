
import express from 'express'
import mysql from "mysql"
import cors from "cors";


const app = express()
// const express = require('express')
app.use(cors());
app.use(express.json())
const db = mysql.createConnection({
    host:"localhost",
    port:'69',
    user:'root',
    password:"C.attano1!",
    database:"testPlease_work"
})

//send informatin to express server


app.get('/',(req, res)=>{
    res.json("BITE THE DUST")
})

//table see if it works
 app.get('/books', (req, res)=>{
    const q ="SELECT * FROM books"
    db.query(q, (err,data )=>{
        if(err) return res.json(err)
        return res.json(data)
    })
 })

 //update the table, add a new book
 app.post('/books', (req, res)=>{
    //                             columns of books
    const q = "INSERT INTO books ('title', 'desc', 'cover') VALUES (?)"
//used postman to figure ut the values were body 
const values = [
    req.body.title,
    req.body.desc,
    req.body.cover,
  ];

 //checks if it when through
    db.query(q,[values],(err,data)=>{
        if(err) return res.send(err)
        return res.json('created sucessfuly')
     })
 })


 //port tyhat I used deslpy the backedn on the web serbver
app.listen(8000, ()=>{
    console.log('THE WORLD')
})