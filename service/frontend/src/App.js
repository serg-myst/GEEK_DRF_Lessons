import React from 'react'
import './App.css'
import UserList from './components/Todousers.js'
import ProjectList from './components/Todoprojects.js'
import TodoList from './components/Todocomments.js'
import Header from './components/Header.js'
import Footer from './components/Footer.js'
import ProjectDetails from './components/ProjectDetails.js'
import axios from 'axios'

import {HashRouter, Link, Route, Switch, Redirect, BrowserRouter} from 'react-router-dom'

const NotFound404 = ({location}) => {
    return (
        <div>
            <hi>Страница по адресу `{location.pathname}` не найдена</hi>
        </div>
    )
}

const MainPage = () => {
    return (
        <div>
            <h3>Подробно</h3>
            <ul>
                <li>
                    <Link to='/users'>Пользователи</Link>
                </li>
                <li>
                    <Link to='/projects'>Проекты</Link>
                </li>
                <li>
                    <Link to='/todo'>Список ToDo</Link>
                </li>
            </ul>
        </div>
    )
}

const Main = () => {
    return (
        <div>
            <Header/>
            <MainPage/>
            <h1>ГЛАВНАЯ СТРАНИЦА</h1>
            <Footer/>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'todo_users': [],
            'todo_projects': [],
            'todo_notes': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                const todo_users = response.data.results
                this.setState(
                    {
                        'todo_users': todo_users
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todoprojects/')
            .then(response => {
                const todo_projects = response.data.results
                console.log(response.data.results)
                this.setState(
                    {
                        'todo_projects': todo_projects
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todonotes/')
            .then(response => {
                const todo_notes = response.data.results
                console.log(response.data.results)
                this.setState(
                    {
                        'todo_notes': todo_notes
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

    // Lesson 5 Убрали, т.к. используем роутеры
    // <UserList todo_users={this.state.todo_users} />
    // <ProjectList todo_projects={this.state.todo_projects} />

    render() {
        return (
            <BrowserRouter>
                <div className='App'>
                    <Switch>
                        <Route exact path='/' component={Main}/>
                        <Route exact path='/users' component={() => <UserList todo_users={this.state.todo_users}/>}/>
                        <Route path='/project/:id'><ProjectDetails todo_projects={this.state.todo_projects}/></Route>
                        <Route exact path='/projects'
                               component={() => <ProjectList todo_projects={this.state.todo_projects}/>}/>
                        <Route exact path='/todo' component={() => <TodoList todo_notes={this.state.todo_notes}/>}/>
                        <Route component={NotFound404}/>
                    </Switch>
                </div>
            </BrowserRouter>)
    }
}

export default App;