import graphene
from files.models import Files
from .types import UploadFileInputType, FileType
import logging
import base64
import uuid
from django.conf import settings
import os
from graphql_jwt.decorators import login_required
from jobs.models import Jobs


logger = logging.getLogger(__name__)

class UploadFile(graphene.Mutation):
    
    file = graphene.Field(FileType, required=True)

    class Arguments:
        input = UploadFileInputType(required=True)

    @login_required
    def mutate(self, info, input):
        try:
            # Get uploaded file data
            base64_content = input.file

            # Decode base64 content
            file_content = base64.b64decode(base64_content)

            unique_id = uuid.uuid4()
            file_name = f"{unique_id}.{input.filename.split('.')[-1]}"  # Generate unique file name

            # Save file to media folder
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            with open(file_path, 'wb') as f:
                f.write(file_content)

            # Construct the file URL
            file_url = os.path.join(settings.MEDIA_URL, file_name)

            # Additional variables
            file_data = {
                'name': file_name,
                'caption': input.filename,
                'mimetype': input.mimetype,
                'url': file_url,
                'user': info.context.user,
            }

            # Check if job_id is provided
            if input.job_id:
                # Retrieve the job object based on the provided job_id
                job = Jobs.objects.get(id=input.job_id)
                file_data['job'] = job

            # Create a new record in the database
            new_file = Files.objects.create(**file_data)

            # Return the created file as the response
            return UploadFile(file=new_file)
        except Exception as e:
            logger.error("Failed to upload file: %s" % e)
            raise Exception("Failed to upload file: %s" % e)


class Mutation(graphene.ObjectType):
    upload_file = UploadFile.Field()