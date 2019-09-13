"""empty message

Revision ID: 3051e27041d4
Revises: 3f17d7baf7e5
Create Date: 2019-09-13 09:25:44.634834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3051e27041d4'
down_revision = '3f17d7baf7e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('notes', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'notes')
    # ### end Alembic commands ###
