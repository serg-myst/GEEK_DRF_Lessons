import React from 'react'
/* import './App.css' */

import 'bootstrap/dist/css/bootstrap.min.css';

import UserList from './components/Todousers.js'
import ProjectList from './components/Todoprojects.js'
import TodoList from './components/Todocomments.js'
import Header from './components/Header.js'
import Footer from './components/Footer.js'
import ProjectDetails from './components/ProjectDetails.js'
import axios from 'axios'

/* Lesson_7 */
import Cookies from 'universal-cookie' /* Установить npm install universal-cookie */
import LoginForm from './components/Auth.js'

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
            'token': [],
            'user': [],
        }
    }

    componentDidMount() {

        this.get_token_from_storage()
        this.load_data()

        /* Lesson_7 Данный код переехал в load_data */
       /* axios.get('http://127.0.0.1:8000/api/todo/')
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
            }).catch(error => console.log(error)) */
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

    get_headers() {
        let headers = {
            'Content-Type': 'application/json',
            /* 'Access-Control-Allow-Headers': 'Content-Type' */
        }

        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    /* Lesson_11 Функция удалить проект. Будем передавать в Totoprojects */
    deleteProject(id) {
        const headers = this.get_headers()
        console.log(headers)
        axios.delete(`http://127.0.0.1:8000/generic/api-projects/delete/${id}`, {headers})
        .then(response => {
        this.setState({todo_projects: this.state.todo_projects.filter((item)=>item.id !==
        id)})
        }).catch(error => console.log(error))
    }

    /* Lesson_7 */
    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated() {
        /* console.log(this.state.token) */
        /* console.log(this.state.token != '') */

        return (this.state.token == '' || this.state.token == undefined) ? false : true

    }

     /* Установим пользователя, который вошел в систему */
    set_user(user) {
        this.setState({'user': user})
    }

    get_user() {
        return (this.state.user == '' || this.state.user == undefined) ? 'Авторизуйтесь' : `Пользователь ${this.state.user}`
    }

    logout() {
        this.set_token('')
        this.set_user('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token})
    }

    refresh_state() {
        let todo_notes = []
        this.setState({'todo_notes': todo_notes})
        let todo_projects = []
        this.setState({'todo_projects': todo_projects})
        let todo_users = []
        this.setState({'todo_users': todo_users})
    }

    load_data() {
        const headers = this.get_headers()
        this.refresh_state()
        /* console.log(this.state.token) */
        axios.get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                const todo_users = response.data.results
                this.setState(
                    {
                        'todo_users': todo_users
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todoprojects/', {headers})
            .then(response => {
                const todo_projects = response.data.results
                /* console.log(response.data.results) */
                this.setState(
                    {
                        'todo_projects': todo_projects
                    }
                )
            }).catch(error => console.log(error))

         axios.get('http://127.0.0.1:8000/api/todonotes/', {headers})
            .then(response => {
                const todo_notes = response.data.results
                console.log(`Заметки ${response.data.results}`)
                this.setState(
                    {
                        'todo_notes': todo_notes
                    }
                )
            }).catch(error => console.log(error))
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
                this.set_user(username)
                }
            ).catch(error => {
                alert('Неверный логи или пароль')
                this.setState({user: []})
                })
    }


    render() {
        return (
            <BrowserRouter>
                <div className='App'>
                    <nav>
                        <div>
                            {this.get_user()}
                        </div>
                        <ul>
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}>Выйти</button> : <Link to='/login'>Войти</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={Main}/>
                        <Route exect path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                        <Route exact path='/users' component={() => <UserList todo_users={this.state.todo_users}/>}/>
                        <Route path='/project/:id'><ProjectDetails todo_projects={this.state.todo_projects}/></Route>
                        <Route exact path='/projects'
                               component={() => <ProjectList todo_projects={this.state.todo_projects}  deleteProject={(id)=>this.deleteProject(id)}/>}/>
                        <Route exact path='/todo' component={() => <TodoList todo_notes={this.state.todo_notes}/>}/>
                        <Route component={NotFound404}/>
                    </Switch>
                </div>
            </BrowserRouter>)
    }
}

export default App;