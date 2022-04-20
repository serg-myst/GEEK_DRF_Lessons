import React from 'react'
import {Link} from "react-router-dom";

class ProjectForm extends React.Component {
    constructor(props) {
    super(props)
    /* 00000000-0000-0000-0000-000000000000 */
    this.state ={
     'Project': {name: '', href: '', description: '', user: []},
     'Project_users': [],
     'isLength': 0
     }
    }

    handleChange(event)
        {
        let Project = this.state.Project
        Project[event.target.name] = event.target.value
        this.setState(
        {
            Project
        }
        );
        }

    handleSubmit(event) {
       this.state.Project_users.forEach((el) => this.state.Project.user.push(el.id))
       this.props.createProject(this.state.Project.name, this.state.Project.href, this.state.Project.description, this.state.Project.user)
        event.preventDefault()
        }

    onClickUser(event){
        let Project_users = this.state.Project_users
        let isLength = this.state.isLength
        let findel = Project_users.indexOf(event.target)
        if (findel === -1) {
            Project_users.push(event.target)
        }
        this.setState({Project_users})
        isLength = Project_users.length
        this.setState({isLength})

    }

    SelectedUser(Project_users) {
      return (<select name="select" size="10">
                    {Project_users.Project_users.map(function(user){
                        return(
                        <option id={user.id} name='user'>{user.innerText}</option>
                        )
                    })
                    }
                </select>
                )
    }

    NoSelectedUsers() {
      return <h3>Выберите пользователей</h3>;
    }

    render() {
        const isLength = this.state.isLength;
        let text
        if (isLength === 0) {
            text = <this.NoSelectedUsers/>
        } else {
            text = <this.SelectedUser  Project_users={this.state.Project_users}/>
        }

        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlFor="login">Название проекта</label>
                    <input type="text" className="form-control" name="name"
                    value={this.state.name} onChange={(event)=>this.handleChange(event)} />
                </div>
                 <div className="form-group">
                    <label htmlFor="href">Ссылка на проект</label>
                    <input type="text" className="form-control" name="href"
                    value={this.state.href} onChange={(event)=>this.handleChange(event)} />
                </div>
                 <div className="form-group">
                    <label htmlFor="description">Описание проекта</label>
                    <input type="text" className="form-control" name="description"
                    value={this.state.description} onChange={(event)=>this.handleChange(event)} />
                </div>
                 <div>
                    <h4>Пользователи проектов</h4>
                    <h4>Кликните по пользователю, чтобы добавить его в новый проект</h4>
                    <select name="select" size="10" onClick={(event) => this.onClickUser(event)}>
                        {this.props.todo_users.map(function(user){
                            return(
                            <option id={user.id} name='user'>{user.username} | {user.email}</option>
                            )
                        })
                        }
                    </select>
                </div>
                <div>
                    <h4>Пользователи проекта</h4>
                    {text}
                </div>
             <input type="submit" className="btn btn-primary" value="Save" />
                <div>
                    <Link to='/projects'>К списку проектов</Link>
                </div>
            </form>
            );
            }
}

export default ProjectForm