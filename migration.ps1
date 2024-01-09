# Configuración de variables
azure_organization=$(azure_organization)
azure_repo=$(azure_repo)
azure_proyect=$(azure_proyect)
azure_username=$(azure_username)
github_username=$(github_username)
github_repo=$(github_repo)
github_token=$(github_token)
azure_pat=$(azure_pat)
azure_branch=$(azure_branch)
github_branch=$(github_branch)
github_email=$(github_email)
github_name=$(github_name)


# Clonar el repositorio de Azure DevOps con autenticación PAT
git clone https://$azure_username:$azure_pat@dev.azure.com/$azure_organization/$azure_proyect/_git/$azure_repo azure_repo
cd azure_repo

# Cambiarse a la rama main en el repositorio de Azure DevOps
git checkout main

# Obtener los cambios desde Azure DevOps
git pull origin main

# Agregar el repositorio de GitHub como remoto
git remote add github_repo https://$github_token@github.com/$github_username/$github_repo.git

git config --global user.email $github_email
git config --global user.name $github_name
git config pull.rebase false  # merge

# Realizar el merge manual
git checkout -b merge-temp main
git merge origin/main

# Resolver conflictos manualmente si los hay

# Realizar el commit de la fusión manual
git commit -m "Merge manual from Azure DevOps"

# Cambiarse a la rama main
git checkout main

# Fusionar el resultado del merge manual
git merge merge-temp

# Ver los cambios
git log

# Obtener los últimos cambios del remoto de GitHub
git pull github_repo main

# Realizar el push
git push github_repo main

# Limpiar
cd ..
rm -rf azure_repo

echo "Merge completado y cambios visibles en la rama main del repositorio de GitHub."