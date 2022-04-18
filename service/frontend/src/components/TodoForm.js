import React from 'react'
import {Link} from "react-router-dom";

class TodoForm extends React.Component {
    constructor(props) {
    super(props)
    this.state ={
        'Todo': {project: '', note_text: '', user: ''},
     }
    }

    handleChange(event){
        let Todo = this.state.Todo
        Todo[event.target.name] = event.target.value
        console.log(Todo)
        this.setState(
        {
            Todo
        }
        );
    }

    Line() {
        return(
            <hr style={{
                            color: '#000000',
                            backgroundColor: '#000000',
                            height: 5
                }}/>
        )
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <h2>Заметка. Необходимо выбрать проект, пользователя и заполнить текст сообщения</h2>
                <div className="form-group">
                    <label htmlFor="project">Выберите проект</label>
                    <select name="project" required="required"  onChange={(event)=>this.handleChange(event)}>
                        <option value="">Выберите значение</option>
                        console.log(this.props.todo_projects)
                            {this.props.todo_projects.map(function(project){
                                return(
                                <option value={project.id} name='project'>{project.name}</option>
                                )
                            })
                      }
                    </select>
                </div>
                <this.Line />
                <div className="form-group">
                    <label htmlFor="user">Выберите пользователя</label>
                    <select name="user" required="required"  onChange={(event)=>this.handleChange(event)}>
                        <option value="">Выберите значение</option>
                            {this.props.todo_users.map(function(user){
                                return(
                                <option value={user.id} name='user'>{user.username} | {user.email}</option>
                                )
                            })
                      }
                    </select>
                </div>
                  <this.Line />
                <div className="form-group">
                    <label htmlFor="note_text">Текст сообщения</label>
                    <p><textarea name="note_text" cols="50" rows="10" onChange={(event)=>this.handleChange(event)}></textarea></p>
                </div>
                <this.Line />
                <input type="submit" className="btn btn-primary" value="Save" />
                <div>
                    <Link to='/todo'>К списку заметок</Link>
                </div>
            </form>
            );
            }
}

export default TodoForm