"""empty message

Revision ID: 165cbae54b1e
Revises: fcc32539e9b2
Create Date: 2019-09-12 11:50:33.516606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '165cbae54b1e'
down_revision = 'fcc32539e9b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('cx_id', sa.Integer(), nullable=False),
    sa.Column('customer_name', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('zip_code', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('phone_num', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('cx_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer')
    # ### end Alembic commands ###
