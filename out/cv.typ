#import "../templates/preamble.typ": *

#show: resume.with(
  author-position: left,
  personal-info-position: left,
  accent-color: "#26428b",
  author: "Name",
  location: "location",
  email: "email@host.com",
  github: "github.com/githubUser",
  linkedin: "https://www.linkedin.com/linkedinUser",
  phone: "+xx xxxxxxx",
  font: "New Computer Modern",
  paper: "us-letter",
)
== Education
#edu(
  institution: "Institution",
  location: "Place",
  dates: "Jan. 20xx - Dec. 20xx",
  degree: "Degree",
)


== Experience
#work(
  title: "Job 1",
  location: "Location",
  company: "Company",
  dates: "Jan 20xx – Dec 20xx",
  description: "- long 
- description",
)

#work(
  title: "Job 2",
  location: "Location",
  company: "Company",
  dates: "Jan 20xx – Dec 20xx",
  description: "- long  description",
)


== Relevant Skills
#generic-two-by-two(
  top-left: strong("Skill category"),
  bottom-left: "skill 1, skill 2",
)


== Language Skills
#generic-one-by-two(
  left: "Language",
  right: "Proficiency",
)


== Selected Projects
#project(
  name: "Project",
  shown_url: "Shown Link",
  full_url: "https://linked_url.com",
  description: "Description",
  technologies: "Stack",
)

#project(
  name: "Small Project",
  description: "Description",
)


== Volunteering
#generic-two-by-two(
  top-left: strong("Type / Title"),
  top-right: "20xx – 20xx",
  bottom-left: "Description",
)


== Awards
#generic-two-by-two(
  top-left: strong("Award Name"),
  top-right: "20xx",
  bottom-left: "Award Description",
)


== Publications
#generic-two-by-two(
  top-left: strong("Publication Title"),
  top-right: "Venue",
  bottom-left: "Author List",
)


