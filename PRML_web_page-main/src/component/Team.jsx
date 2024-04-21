import React from 'react'
import { ImGithub } from "react-icons/im";
import { IoLogoLinkedin } from "react-icons/io";
import test from '../Image/test.png'
import advait from '../Image/Advait.jpg'
import aniket from '../Image/Aniket.jpg'
import qazi from '../Image/Qazi.jpg'
import aditya from '../Image/Aditya.jpg'
import aansh from '../Image/aansh.jpg'

function Team() {
    const teams=[
        {
            name:"Advait Gaur",
            img:advait,
            github:"https://github.com/Advaitgaur004"
        },
        {
            name:"Aniket Singh",
            img:aniket,
            github:"https://github.com/aniket170105"
        },
        {
            name:"Qazi Talha",
            img:qazi,
            github:"https://github.com/Qazi-Talha-Ali-087"
        },
        {
            name:"Aditya Padhy",
            img:aditya,
            github:"https://github.com/aditya-padhy"
        },
        {
            name:"Aansh Dubey",
            img:aansh,
            github:"https://github.com/QuantTitan"
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
                <a href={team.github} target="_blank" rel="noopener noreferrer"> <ImGithub  size={30} color='black' style={{marginRight:"15px"}}/></a>
                {/* Add LinkedIn link if available */}
                {/* <a href={team.linkdin} target="_blank" rel="noopener noreferrer"> <IoLogoLinkedin size={30} color='black'/></a> */}
            </div>
            ))}
        </div>
    </div>
  )
}

export default Team
