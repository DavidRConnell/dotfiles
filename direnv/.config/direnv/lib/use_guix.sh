use_guix() {
    # Generate an enviornment from a list of guix manifests and save
    # the resulting profile. If a profile already exists and was
    # created after all of the manifests were last edited, enter an
    # enviornment with only that profile. Otherwise, create a new
    # profile.
    #
    # BUG: if a manifest is passed to this function that wasn't used
    # to create the project's profile and is older than the profile,
    # the profile will be sourced instead of remade, resulting in a
    # profile without the extra manifests enviornment variables. In
    # this case, manually remove the project's profile or touch a
    # manifest and rerun.

    local profile_name="$(basename $PWD)"
    local profile_dir="$GUIX_PROFILE_PATH/$profile_name"
    GUIX_PROFILE="$profile_dir/$profile_name"

    newer_than () {
        # -nt conditional failed. possibly because $gcroot is a link and
        # the modification date of the file it's linked to is 1969.
        [[ $(stat -c %y "$1") > $(stat -c %y "$2") ]]
    }

    [ -e "$profile_dir" ] || mkdir -p "$profile_dir"

    local is_profile_fresh="false"
    [ -e "$GUIX_PROFILE" ] && is_profile_fresh="true"

    local manifests=""
    for manifest in "$@"; do
        [ "$is_profile_fresh" = "true" ] && \
            newer_than "$GUIX_PROFILE" "$manifest" || \
            is_profile_fresh="false"

        if [ ! -e "$manifest" ]; then
            echo "Warning $manifest not found skipping..." >&2
        else
            manifests="-m $manifest $manifests"
        fi
    done

    if [ -z "$manifests" ]; then
        echo "Warning no $manifests found. Not changing enviornment" >&2
        exit 1
    elif [ "$is_profile_fresh" = "false" ]; then
        echo "Updating stale profile..." >&2
        eval "$(guix package --profile=$GUIX_PROFILE $manifests)"
    fi

    source $GUIX_PROFILE/etc/profile
}
