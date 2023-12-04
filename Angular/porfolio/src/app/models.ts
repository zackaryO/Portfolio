// models.ts

export interface AboutMe {
    // Define the properties of the AboutMe data structure
    id: number;
    title: string;
    introduction: string;
}

export interface Education {
    id: number;
    schoolName: string;
    degree: string;
    startDate: Date;
    endDate: Date;
}

export interface Experience {
    id: number;
    jobTitle: string;
    companyName: string;
    startDate: Date;
    endDate: Date;
    description: string;
}

export interface Skill {
    id: number;
    name: string;
    proficiencyLevel: string;
    categoryId: number;
}

export interface Resume {
    id: number;
    name: string;
    email: string;
    phone: string;
    summary: string;
    education: Education[];
    experience: Experience[];
    skills: Skill[];
}

export interface Project {
    id: number;
    title: string;
    description: string;
    image: string;
    link: URL;
}

export interface ContactInfo {
    id: number;
    email: string;
    phone: string;
    location: string;
}

export interface SocialMediaLink {
    id: number;
    platformName: string;
    url: URL;
    icon: string;
}

