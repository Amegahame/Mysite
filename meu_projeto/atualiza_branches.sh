branches=("models" "django-admin" "Views" "Project-setup" "templates")

# Atualiza a main
git checkout main
git pull origin main

# Para cada branch, faz checkout, merge e push
for branch in "${branches[@]}"; do
    echo "=============================="
    echo "🚀 Atualizando a branch: $branch"

    # Verifica se há mudanças pendentes
    if [[ -n $(git status --porcelain) ]]; then
        echo "⚠️ Existem alterações não commitadas. Faça commit ou stash antes de prosseguir."
        exit 1
    fi

    git checkout $branch
    git pull origin $branch
    git merge main

    git push origin $branch

    echo "✅ Branch $branch atualizada!"
    echo "=============================="
done
