import React from 'react'
import './App.css'
import UserList from './components/Todousers.js'
import Header from './components/Header.js'
import Footer from './components/Footer.js'
import axios from 'axios'

class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'todo_users': []
       }
 }

   componentDidMount() {
       axios.get('http://127.0.0.1:8000/api/todo/')
           .then(response => {
               const todo_users = response.data
               console.log(response.data)
                   this.setState(
                   {
                       'todo_users': todo_users
                   }
               )
           }).catch(error => console.log(error))
 }

   // componentDidMount() {
   //     const todo_users = [
   //     {
   //         'email': 'email@mail.ru',
   //         'first_name': 'Name',
   //         'last_name': 'LastName',
   //         'birthday_year': 2000
   //     },
   //     {
   //         'email': 'email1@mail.ru',
   //         'first_name': 'Name1',
   //         'last_name': 'LastName1',
   //         'birthday_year': 2001
   //     },
   //     ]
   //     this.setState(
   //     {
   //        'todo_users': todo_users
   //     }
   //     )
   // }

   render () {
       return (
           <div>
               <Header />
               <UserList todo_users={this.state.todo_users} />
               <Footer />
           </div>
       )
   }
}

export default App;
