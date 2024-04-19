import React from 'react'
import { ImGithub } from "react-icons/im";
import { IoLogoLinkedin } from "react-icons/io";
import test from '../Image/test.png'
function Team() {
    const teams=[
        {
            name:"Advait gaur",
            img:test,
            linkdin:"",
            github:""
        },
        {
            name:"Aniket Singh",
            img:test,
            linkdin:"",
            github:""
        },
        {
            name:"Qazi Talha",
            img:test,
            linkdin:"",
            github:""
        },
        {
            name:"Aditya Padhy",
            img:test,
            linkdin:"",
            github:""
        },
        {
            name:"Aansh Dubey",
            img:test,
            linkdin:"",
            github:""
        },
    ]
  return (
    <div>
            <p className='header_Problem'>Team</p>
            <div className='container'>
                {teams.map((team,index)=>(
                    
                <div key={index} className='profile_container'>
                    <img src={`${team.img}`} alt="" className='prfile_pic'/>
                    <h4>{team.name}</h4>
                    <a href="http://www.google.com" target="_blank" rel="noopener noreferrer"> <ImGithub  size={30} color='black'style={{marginRight:"15px"}}/></a>
                    <a href="http://www.google.com" target="_blank" rel="noopener noreferrer"> <IoLogoLinkedin size={30} color='black'/></a>

                </div>
                ))}
            </div>

    </div>
  )
}

export default Team
